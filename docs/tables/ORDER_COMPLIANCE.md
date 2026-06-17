# ORDER_COMPLIANCE

> Stores the information for patient compliance of orders that are within the system.

**Description:** Order Compliance  
**Table type:** ACTIVITY  
**Primary key:** `ORDER_COMPLIANCE_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_COMPLIANCE_STATUS_FLAG` | DOUBLE | NOT NULL |  | The compliance status for the encounter. 0 - Complete, 1 - Incomplete, 2 - In Error |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encounter that the compliance was captured for. |
| 3 | `NO_KNOWN_HOME_MEDS_IND` | DOUBLE | NOT NULL |  | Indicates that no know home medications were present for a patient at the time the compliance was captured. |
| 4 | `ORDER_COMPLIANCE_ID` | DOUBLE | NOT NULL | PK | The primary key of this table |
| 5 | `PERFORMED_DT_TM` | DATETIME | NOT NULL |  | The date and time the compliance was captured. |
| 6 | `PERFORMED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel that captured the patient compliance. |
| 7 | `PERFORMED_TZ` | DOUBLE | NOT NULL |  | The time zone the personnel was in when the compliance information was captured. |
| 8 | `UNABLE_TO_OBTAIN_IND` | DOUBLE | NOT NULL |  | Indicates that no information was able to be obtained for any order during the time that the compliance was captured. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERFORMED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ORDER_COMPLIANCE_DETAIL](ORDER_COMPLIANCE_DETAIL.md) | `ORDER_COMPLIANCE_ID` |

