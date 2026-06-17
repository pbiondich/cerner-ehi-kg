# RAD_FOLD_TRANS_RULE

> The Rad_Fold_Trans_Rule table contains the user define rules that are used while executing a batch transfer of folders within the image management area.

**Description:** Rad Folder Transfer Rule  
**Table type:** REFERENCE  
**Primary key:** `TRANS_RULE_ID`  
**Columns:** 27  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACT_FREQ_FLAG` | DOUBLE |  |  | The Act_Freq_Flag indicates the unit of time that is used to determine the order activity criteria. (ex: daily, weekly, monthly, yearly) |
| 3 | `ACT_FREQ_INTERVAL` | DOUBLE |  |  | the Act_Freq_Interval indicates the number to be used along with the unit of time from the Act_Freq_Flag. For example if the flag indicates monthly, and the interval is 2, then the frequency would be every 2 months. |
| 4 | `AGE_LIMIT_IND` | DOUBLE |  |  | Indicates whether a rule has an Age_limit |
| 5 | `BEGIN_DT_TM` | DATETIME |  |  | The Begin_Dt_Tm identifies when the frequency that was specified should begin. |
| 6 | `EXCLUDE_DECEASED_IND` | DOUBLE |  |  | The Exclude_Deceased_Ind field indicates whether or not to exclude folders for a deceased patient. |
| 7 | `EXCLUDE_INTCASE_IND` | DOUBLE |  |  | The Exclude_IntCase_Ind field indicates whether or not to exclude folders that contain exams that have been marked as an interesting case. |
| 8 | `EXCLUDE_MEDLEGAL_IND` | DOUBLE |  |  | The Exclude_MedLegal_Ind field indicates whether or not to exclude folders that contain exams that have been marked for medical legal purposes. |
| 9 | `FRI_IND` | DOUBLE |  |  | The Fri_Ind field indicates if Friday is a day that the transfer rule is to be run. |
| 10 | `FROM_LIB_CD` | DOUBLE | NOT NULL | FK→ | The From_Lib_Cd is a foreign key to the Track_Pt_Library table. It identifies the Library that folders are going to be moved from. |
| 11 | `MAX_FOLD_CUTOFF` | VARCHAR(100) |  |  | the Max_Fold_Cutoff field contains a folder number used when qualifying folders for transfer. For example, all folders with a folder number less than 1234567. |
| 12 | `MON_IND` | DOUBLE |  |  | The Mon_Ind field indicates if Monday is a day that the transfer rule is to be run. |
| 13 | `PRIOR_DT_TM` | DATETIME |  |  | The Prior_Dt_Tm contains a date and time that should be used when checking for order activity. For example, all folders that have not had activity since 12/12/96. |
| 14 | `PULL_FREQ_FLAG` | DOUBLE |  |  | The Pull_Freq_Flag indicates the unit of time that is used to determine the print frequency for the pull list. (ex: daily, weekly, monthly, yearly) |
| 15 | `PULL_FREQ_INTERVAL` | DOUBLE |  |  | the Pull_Freq_Interval indicates the number to be used along with the unit of time from the Pull_Freq_Flag. For example if the flag indicates monthly, and the interval is 2, then the frequency wouldbe every 2 months. |
| 16 | `SAT_IND` | DOUBLE |  |  | The Sat_Ind field indicates if Saturday is a day that the transfer rule is to be run. |
| 17 | `SUN_IND` | DOUBLE |  |  | The Sun_Ind field indicates if Sunday is a day that the transfer rule is to be run. |
| 18 | `THU_IND` | DOUBLE |  |  | The Thu_Ind field indicates if Thursday is a day that the transfer rule is to be run. |
| 19 | `TO_LIB_CD` | DOUBLE | NOT NULL | FK→ | The To_Lib_Cd is a foreign key to the Track_Pt_Library table. It identifies the Library that folders are going to be moved to. |
| 20 | `TRANS_RULE_ID` | DOUBLE | NOT NULL | PK | The trans_rule_id is a unique, meaningless number that serves no other purpose other than a unique identifier. |
| 21 | `TUE_IND` | DOUBLE |  |  | The Tue_Ind field indicates if Tuesday is a day that the transfer rule is to be run. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 27 | `WED_IND` | DOUBLE |  |  | The Wed_Ind field indicates if Wednesday is a day that the transfer rule is to be run. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FROM_LIB_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `TO_LIB_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [PULL_TRANS_REQ](PULL_TRANS_REQ.md) | `TRANS_RULE_ID` |
| [TRANS_EXAM_EXCLUSIONS](TRANS_EXAM_EXCLUSIONS.md) | `TRANS_RULE_ID` |
| [TRANS_FOLD_EXCLUSIONS](TRANS_FOLD_EXCLUSIONS.md) | `TRANS_RULE_ID` |

