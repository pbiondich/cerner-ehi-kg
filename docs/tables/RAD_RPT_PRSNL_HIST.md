# RAD_RPT_PRSNL_HIST

> Radiology Report Personnel History

**Description:** This table contains a cumulative list of prsnl that have taken action on the rep  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_CD` | DOUBLE | NOT NULL |  | This column represents the action that the personnel took on a given radiology report. |
| 2 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | This column contains the date and time that the prsnl took an action on a given radiology report. |
| 3 | `ACTION_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 4 | `PROXIED_FOR_ID` | DOUBLE | NOT NULL | FK→ | This column is only valued if the action was Proxy. It indicates who was proxied for. |
| 5 | `RAD_REPORT_ID` | DOUBLE | NOT NULL | FK→ | This column contains a foreign key to the Rad_Report table. It uniquely identifies the report that the personnel are associated with. |
| 6 | `REPORT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This column contains a foreign key to the Prsnl table. It uniquely identifies the personnel that is associated with a given radiology report. |
| 7 | `RPT_PRSNL_HIST_ID` | DOUBLE | NOT NULL |  | This column contains a meaningless number that only serves to uniquely identify a row on the rad_rpt_prsnl_hist table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROXIED_FOR_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RAD_REPORT_ID` | [RAD_REPORT](RAD_REPORT.md) | `RAD_REPORT_ID` |
| `REPORT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

