
# Lab4-Twizz

## Who Did What

| Member | GitHub Username | File |
|---|---|---|
| Zaw Ye Yint Htoo | johnfredifre-sys | test_deposit.py |
| Hnin Ei Ei Win | winniehnin | test_withdraw.py |
| Saw James Htun Hla Baw | James2k8 | test_shared.py |
| Khin Sandar Htun | 6705142033-ux | test_teardown.py |

## Our Merge Conflict

 Conflict Markers Encountered: We encountered `<<<<<<< HEAD` representing local changes, `=======` separating the versions, and `>>>>>>> cc92ffb11657bf4f96a21e0de90aa62e7315ba15` showing the incoming changes from the remote repository[cite: 5].
 Final Decision: We decided to keep both sets of changes[cite: 1, 5]. For the title section, we kept `# Lab4-Twizz`[cite: 5], and for the table, we accepted both changes so that every group member's row (`Zaw Ye Yint Htoo`, `Winnie`, and `Saw James Htun Hla Baw`) appeared in the final document[cite: 1, 5].
 Why Git Couldn't Resolve It Automatically: Git could not resolve the conflict automatically because group members modified the same lines in `README.md` simultaneously[cite: 1, 5]. Since Git cannot know which team member's content should take precedence, human intervention was required to merge the lines[cite: 1].


5  Zaw Ye Yint Htoo
     4  Khin Sandar
     4  winniehnin
     3  James2k8
     2  johnfredifre-sys
     1  Arnt Htoo Lwin


## (5)Reflection question

1.Our push got blocked because a teammate had already pushed new commits to GitHub that weren't on our local machine yet. We fixed it by running git pull origin main to fetch those updates, resolving the merge conflicts that popped up, and then pushing again.

2.Git couldn't automatically merge the README.md file because different team members edited the exact same lines at the same time. Since Git doesn't know whose changes to prioritize, it paused and asked us to manually choose what to keep.

3.Committing creates a local snapshot of your changes on your own computer, while pushing actually uploads those saved commits to the shared remote repository on GitHub.

4.Fixtures let you define common setup tasks and sample data once so they can be reused across multiple tests automatically. This keeps your test files clean and saves you from writing the same initialization code over and over.

