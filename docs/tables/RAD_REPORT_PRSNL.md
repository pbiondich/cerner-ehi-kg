# RAD_REPORT_PRSNL

> The Rad_Report_Prsnl table keeps track of all of the people that have interacted, or will interact, with a radiology report.

**Description:** Rad Report Prsnl  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | The Action_Dt_Tm captures the date and time that the person finished their involvement with the report. |
| 2 | `ACTION_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 3 | `PROVISIONAL_QUEUE_IND` | DOUBLE | NOT NULL |  | The Provisional_Queue_Ind indicates if the report is currently queued to this person in the provisional queue. |
| 4 | `PROXIED_FOR_ID` | DOUBLE | NOT NULL | FK→ | The Proxied_For_Id contains the Id of the person that was proxied for by this individual. |
| 5 | `PRSNL_RELATION_FLAG` | DOUBLE | NOT NULL |  | The Prsnl_Relation_Flag indicates the relationship that the person had with the report. (ex. transcriptionist, radiologist, resident) |
| 6 | `QUEUE_IND` | DOUBLE |  |  | The Queue_Ind indicates if the report is currently queued to this person. |
| 7 | `RAD_REPORT_ID` | DOUBLE | NOT NULL | FK→ | The Rad_Report_Id is a foreign key to the Rad_Report table. It identifies the report that the person is related to. |
| 8 | `REPORT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The Report_Prsnl_Id is a foreign key to the Prsnl table. It identifies the person that is related to the report. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROXIED_FOR_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RAD_REPORT_ID` | [RAD_REPORT](RAD_REPORT.md) | `RAD_REPORT_ID` |
| `REPORT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

