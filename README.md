# Lab4-Twizz

## Who Did What

| Member | GitHub Username | File |
|---|---|---|
| Zaw Ye Yint Htoo | johnfredifre-sys | test_deposit.py, conftest.py |
| Hnin Ei Ei Win | winniehnin | test_withdraw.py |
| Saw James Htun Hla Baw | sjames-cpu | test_shared.py |
| Khin Sandar Htun | 6705142033-ux | test_teardown.py |

## Our Merge Conflict

We edited the same lines of README.md in separate local copies. One member pushed first, so my push was rejected. When I ran `git pull --no-rebase`, Git showed the local and incoming versions between <code>&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD</code>, <code>&#61;&#61;&#61;&#61;&#61;&#61;&#61;</code>, and <code>&gt;&gt;&gt;&gt;&gt;&gt;&gt; 928a4a6</code>.

Git could not choose a version automatically because our edits overlapped. We removed the conflict markers, kept all four members' rows, and used my full name in the final table.

## Git Contribution Summary

Output of `git shortlog -sn` before this README correction:

```text
     7  Zaw Ye Yint Htoo
     7  winniehnin
     4  Khin Sandar
     3  James2k8
     2  johnfredifre-sys
     1  Arnt Htoo Lwin
```

Arnt Htoo Lwin made an earlier commit but later left the group. The two author names Zaw Ye Yint Htoo and johnfredifre-sys use the same Git email.

## Reflection Questions

1. **Why was your push rejected, and how did you fix it?** A teammate pushed first, so my local repository was behind GitHub. I pulled the new commits, resolved the README conflict, committed the merge, and pushed again.

2. **Why could Git not resolve the README conflict automatically?** We changed the same lines in different copies of README.md. Git needed us to decide which content to keep.

3. **What is the difference between committing and pushing?** Committing saves changes in my local repository. Pushing uploads those commits to GitHub for my teammates to see.

4. **How do fixtures reduce duplicated setup code in tests?** A fixture prepares the account for each test, so we do not have to repeat the same setup code in every test.

