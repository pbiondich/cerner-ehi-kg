# PLM_TAT_PARAMETER

> This table contains reference turnaround and specimen expiration minutes for orderables (for different service resources and reporting priorities)

**Description:** Turnaround Time parameters  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALERT_MIN` | DOUBLE | NOT NULL |  | Minutes, from In-lab to when the Orderable gets to an Alert time. OR Minutes from Drawn_dt_tm to when the specimen gets to an Expire Time for Specimen Expiration (for specimen expiration times) |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The catalog_cd of the orderable that is being performed at the Service_resource |
| 5 | `DISPLAY_MIN` | DOUBLE | NOT NULL |  | Minutes from In -lab to when the Orderable gets to a Display time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `REP_PRIORITY_CD` | DOUBLE | NOT NULL |  | The Reporting Priority codes for the Turn around times from codeset 1905. This is zero for the Specimen expiration times. |
| 8 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | The subsection, bench or the instrument for which the times are built. |
| 9 | `TAT_ID` | DOUBLE | NOT NULL |  | This is a sequential id which will be unique for each rule. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `WARNING_MIN` | DOUBLE | NOT NULL |  | Minutes from In-lab to when the Orderable gets to a Warning time for Turn Around Times. Minutes from Drawn_dt_tm to when the specimen gets to a Warning Time (for Specimen Expiration) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

