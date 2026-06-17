# OMF_RADREPORT_ST

> Contains the various date/time fields (transcribed, final) and corresponding personnel associated to report, when its transcribed , addended and final.

**Description:** OMF Rad Report Summary Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DICTATE_DT_NBR` | DOUBLE | NOT NULL |  | Contains the "Date number" value, corresponding to the Dictate Dt/Tm |
| 2 | `DICTATE_DT_TM` | DATETIME |  |  | Contains the date and time at which the report was dictated. |
| 3 | `DICTATE_MIN_NBR` | DOUBLE | NOT NULL |  | Contains the "Minute number" value, corresponding to the Dictate Dt/tm |
| 4 | `DICTATE_TZ` | DOUBLE | NOT NULL |  | Contains the time zone value, corresponding the Dictate Dt/tm saved. |
| 5 | `FINAL_DT_NBR` | DOUBLE | NOT NULL |  | Contains the "Date number" value, corresponding to the Final Dt/Tm |
| 6 | `FINAL_DT_TM` | DATETIME |  |  | Contains the date and time at which the report is made final. |
| 7 | `FINAL_MIN_NBR` | DOUBLE | NOT NULL |  | Contains the "Minute number" value, corresponding to the Final Dt/tm |
| 8 | `FINAL_TZ` | DOUBLE | NOT NULL |  | Contains the time zone value, corresponding the Final Dt/tm saved. |
| 9 | `OMF_RADREPORT_ST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the OMF_RADREPORT_ST table. |
| 10 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This is foreign key to the orders table, will contain the order_ID of the selected exam. |
| 11 | `PROXY_ID` | DOUBLE | NOT NULL | FK→ | Contains the personnel ID of the proxy associated to the report of the selected order. This is foreign key to the Prsnl table. |
| 12 | `RADIOLOGIST_ID` | DOUBLE | NOT NULL | FK→ | Contains the personnel ID of the Radiologist associated to the report of the selected order. This is foreign key to the Prsnl table. |
| 13 | `RAD_REPORT_ID` | DOUBLE | NOT NULL | FK→ | Composite key along with order_ID. This is a foreign key to rad_report table, will contain the report_ID of the selected exam. |
| 14 | `REPORT_STATUS_FLAG` | DOUBLE | NOT NULL |  | This denotes if the selected report is in transcribed/modified status or in addended/correction status. If report_ID of the selected row corresponds to transcribed/modified report then this flag will be equal to 0. And if the report of the selected row corresponds to addended/corrected then this flag will be equal to 1. |
| 15 | `RESIDENT_ID` | DOUBLE | NOT NULL | FK→ | Contains the personnel ID of the Resident associated to the report of the selected order. This is foreign key to the Prsnl table. |
| 16 | `TRANSCRIBE_DT_NBR` | DOUBLE | NOT NULL |  | Contains the "Date number" value, corresponding to the transcribed Dt/Tm. |
| 17 | `TRANSCRIBE_DT_TM` | DATETIME |  |  | Contains the date and time at which the report is transcribed.. |
| 18 | `TRANSCRIBE_MIN_NBR` | DOUBLE | NOT NULL |  | Contains the "Minute number" value, corresponding to the transcribed Dt/tm. |
| 19 | `TRANSCRIBE_TZ` | DOUBLE | NOT NULL |  | Contains the time zone value, corresponding the transcribed Dt/tm saved. |
| 20 | `TRANSCRIPTIONIST_ID` | DOUBLE | NOT NULL | FK→ | Contains the personnel ID of the user responsible for transcribing the report. This is foreign key to the Prsnl table. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PROXY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RADIOLOGIST_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RAD_REPORT_ID` | [RAD_REPORT](RAD_REPORT.md) | `RAD_REPORT_ID` |
| `RESIDENT_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TRANSCRIPTIONIST_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

