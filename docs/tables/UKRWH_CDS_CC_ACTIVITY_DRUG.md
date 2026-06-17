# UKRWH_CDS_CC_ACTIVITY_DRUG

> Contains details for the use of high cost drugs as per OPCS-4 definitions provided per Critical Care Activity.

**Description:** UKRWH_CDS_CC_ACTIVITY_DRUG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) |  |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 3 | `DRUG_SEQ` | DOUBLE |  |  | Number between 1-20 that uniquely identifies the use of a high cost drug within a critical care activity when combined with UKRWH_CARE_ACTIVITY_KEY. |
| 4 | `DRUG_VALUE` | VARCHAR(40) |  |  | This is the OPCS-4 definition for a high cost drug used as part of a CRITICAL CARE ACTIVITY. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | First date/time row was inserted into table. |
| 6 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 7 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Last date/time row was updated. |
| 9 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 10 | `UKRWH_CDS_CC_ACTIVITY_DRUG_KEY` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the UKRWH_CDS_CC_ACTIVITY_DRUG table. |
| 11 | `UKRWH_CDS_CC_ACTIVITY_KEY` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the UKRWH_CRITICAL_CARE_ACTIVITY table. |
| 12 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_TASK` | VARCHAR(40) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

