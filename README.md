# Lab4-Twizz

## Group Name

Lab4-Twizz

## Who Did What

| Member | GitHub Username | File |
|---|---|---|
| Zaw Ye Yint Htoo | johnfredifre-sys | bank.py, .gitignore, test_deposit.py, conftest.py |
| Hnin Ei Ei Win | winniehnin | test_withdraw.py |
| Saw James Htun Hla Baw | sjames-cpu | test_shared.py |
| Khin Sandar Htun | 6705142033-ux | test_teardown.py |

## Our Merge Conflict

### What happened

During Round 3, group members edited the same part of `README.md` in separate local copies. After one member pushed, another push was rejected because the remote repository had newer commits. Pulling those commits produced a README merge conflict.

### Conflict markers encountered

Git placed the two versions between <code>&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD</code>, <code>&#61;&#61;&#61;&#61;&#61;&#61;&#61;</code>, and <code>&gt;&gt;&gt;&gt;&gt;&gt;&gt; 928a4a6</code>. The conflicting versions included the `test_withdraw.py` and `test_shared.py` rows. Later README edits also involved the other members' rows.

### Final decision

We removed the conflict markers and kept the information for all four current members. We checked the names and GitHub usernames in the final table. The repository history records the README merges, including commits `cc92ffb` and `fec6dc4`.

### Why Git could not merge automatically

Members changed the same lines of the README table in different copies of the repository. Git could see both versions but could not decide which rows the group intended to keep, so we combined the changes manually.

## Git Contribution Summary

This is a snapshot of `git shortlog -sn` taken before the final README corrections:

```text
     7  Zaw Ye Yint Htoo
     7  winniehnin
     4  Khin Sandar
     3  James2k8
     2  johnfredifre-sys
     1  Arnt Htoo Lwin
```

Arnt Htoo Lwin made an earlier commit but later left the group. `Zaw Ye Yint Htoo` and `johnfredifre-sys` used the same Git email, but Git lists their author names separately.

## Reflection Questions

1. **Why was our push rejected, and how did we fix it?** A teammate pushed new commits first, so our local copy was behind GitHub. We pulled the changes, resolved the README conflict, committed the merge, and pushed again.

2. **Why could Git not resolve the README conflict automatically?** Several members edited the same lines of `README.md` in separate copies. Git needed us to decide how to combine those changes.

3. **What is the difference between committing and pushing?** Committing saves changes in a local repository. Pushing uploads local commits to the shared GitHub repository so other members can access them.

4. **How do fixtures reduce duplicated setup code in tests?** Fixtures prepare reusable test data, such as a bank account. Each test can use the fixture instead of repeating the same setup code.