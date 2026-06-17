# OMF_RULES

> Holds rules which the calc engine uses to determine if a row "qualifies."

**Description:** OMF RULES  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BEG_EVENT_NUM` | DOUBLE |  |  | The first clinical event (e.g. Ordered, Drawn, Verified) defined in the rule - specific to TAT. |
| 7 | `DESCRIPTION` | VARCHAR(80) |  |  | Rule/Study description |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `PRIORITY` | DOUBLE |  |  | If multiple rules can be used (as in TAT) which will be used first |
| 10 | `PRODUCT_CD` | DOUBLE |  |  | Product this rule is used with. Typically a code value for Infection Control or TAT |
| 11 | `PROSE` | VARCHAR(255) |  |  | The rule as it can be displayed. E.g. Source=Blood and Organism=E. Coli |
| 12 | `RULE_ID` | DOUBLE | NOT NULL |  | Unique rule identifier |
| 13 | `RULE_SEQ` | DOUBLE | NOT NULL |  | Used if the rules prose (or other fields) are > 255 characters |
| 14 | `TIME_BLK_BEG_TIME` | VARCHAR(8) |  |  | Beginning time of the time block. |
| 15 | `TIME_BLK_END_TIME` | VARCHAR(8) |  |  | Ending time of the time block. |
| 16 | `TIME_BLK_EVENT_NUM` | DOUBLE |  |  | Event number for the beginning of the time block such as for ORDER, DRAWN, COMPLETE, etc. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

