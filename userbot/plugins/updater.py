"""Update UserBot code
Syntax: .update"""

import git
from contextlib import suppress
import os
import sys
import asyncio
from userbot.utils import admin_cmd

# -- Constants -- #
IS_SELECTED_DIFFERENT_BRANCH = (
    "Looks like a custom branch {branch_name} "
    "Is being used:\n"
    "In this case, Updater is unable to identify the branch to be updated."
    "Please check out to an official branch, and re-start the updater."
)
OFFICIAL_UPSTREAM_REPO = "https://github.com/StarkGang/FridayUserbot/"
BOT_IS_UP_TO_DATE = "**Boss! My System is already Upgraded!**."
NEW_BOT_UP_DATE_FOUND = (
    "Boss I found update for {branch_name}\n"
    "{changelog}\n"
    "**Ok Boss ! I Am Trying To Pull Update**"
)
NEW_UP_DATE_FOUND = (
    "**Boss I Found new update found for {branch_name}**\n"
    "`i am updating ...`"
)
REPO_REMOTE_NAME = "temponame"
IFFUCI_ACTIVE_BRANCH_NAME = "master"
DIFF_MARKER = "HEAD..{remote_name}/{branch_name}"
NO_HEROKU_APP_CFGD = "Boss ! no heroku application found, but a key given? 😕 "
HEROKU_GIT_REF_SPEC = "HEAD:refs/heads/master"
RESTARTING_APP = "Boss ! I am Restarting "
# -- Constants End -- #


#@command(pattern="^.update", outgoing=True)
@borg.on(admin_cmd(pattern=r"update"))
async def updater(message):
    try:
        repo = git.Repo()
    except git.exc.InvalidGitRepositoryError as e:
        repo = git.Repo.init()
        origin = repo.create_remote(REPO_REMOTE_NAME, OFFICIAL_UPSTREAM_REPO)
        origin.fetch()
        repo.create_head(IFFUCI_ACTIVE_BRANCH_NAME, origin.refs.master)
        repo.heads.master.checkout(True)

    active_branch_name = repo.active_branch.name
    if active_branch_name != IFFUCI_ACTIVE_BRANCH_NAME:
        await message.edit(IS_SELECTED_DIFFERENT_BRANCH.format(
            branch_name=active_branch_name
        ))
        return False

    try:
        repo.create_remote(REPO_REMOTE_NAME, OFFICIAL_UPSTREAM_REPO)
    except Exception as e:
        print(e)
        pass

    temp_upstream_remote = repo.remote(REPO_REMOTE_NAME)
    temp_upstream_remote.fetch(active_branch_name)

    changelog = generate_change_log(
        repo,
        DIFF_MARKER.format(
            remote_name=REPO_REMOTE_NAME,
            branch_name=active_branch_name
        )
    )

    if not changelog:
        await message.edit("**Boss i Found UPDATE Let me Upgrade Myself To Serve You Better!!...**")
        await asyncio.sleep(8)
 
    message_one = NEW_BOT_UP_DATE_FOUND.format(
        branch_name=active_branch_name,
        changelog=changelog
    )
    message_two = NEW_UP_DATE_FOUND.format(
        branch_name=active_branch_name
    )

    if len(message_one) > 4095:
        with open("change.log", "w+", encoding="utf8") as out_file:
            out_file.write(str(message_one))
        await bot.send_message(
            message.chat_id,
            document="change.log",
            caption=message_two
        )
        os.remove("change.log")
    else:
        await message.edit(message_one)

    temp_upstream_remote.fetch(active_branch_name)
    repo.git.reset("--hard", "FETCH_HEAD")

    if Var.HEROKU_API_KEY is not None:
        import heroku3
        heroku = heroku3.from_key(Var.HEROKU_API_KEY)
        heroku_applications = heroku.apps()
        if len(heroku_applications) >= 1:
            if Var.HEROKU_APP_NAME is not None:
                heroku_app = None
                for i in heroku_applications:
                    if i.name == Var.HEROKU_APP_NAME:
                        heroku_app = i
                if heroku_app is None:
                    await message.edit("Boss ! Invalid APP Name. Boss Please set the name of your bot in heroku in the var HEROKU_APP_NAME.")
                    return
                heroku_git_url = heroku_app.git_url.replace(
                    "https://",
                    "https://api:" + Var.HEROKU_API_KEY + "@"
                )
                if "heroku" in repo.remotes:
                    remote = repo.remote("heroku")
                    remote.set_url(heroku_git_url)
                else:
                    remote = repo.create_remote("heroku", heroku_git_url)
                asyncio.get_event_loop().create_task(deploy_start(bot, message, HEROKU_GIT_REF_SPEC, remote))

            else:
                await message.edit("Boss ! Please create the var HEROKU_APP_NAME as the key and the name of your bot in heroku as your value.")
                return
        else:
            await message.edit(NO_HEROKU_APP_CFGD)
    else:
        await message.edit("Boss ! I Found No heroku api key found in HEROKU_API_KEY var")
        

def generate_change_log(git_repo, diff_marker):
    out_put_str = ""
    d_form = "%d/%m/%y"
    for repo_change in git_repo.iter_commits(diff_marker):
        out_put_str += f"❥︎[{repo_change.committed_datetime.strftime(d_form)}]➪︎ {repo_change.summary} ✪︎{repo_change.author}\n"
    return out_put_str

async def deploy_start(bot, message, refspec, remote):
    await message.edit(RESTARTING_APP)
    await message.edit("**Boss! I Am Upgraded Now I Am Trying A Restart do** `.alive` **to check if I am Alive Or Dead**\nIt will takes approximately 5 mins to update My Software!!\nBoss Thank You For Using Me You Are My Best Boss!!,")
    await remote.push(refspec=refspec)
    await bot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)

    
