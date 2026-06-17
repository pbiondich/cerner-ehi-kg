# BR_PQRS_MEAS

> The measures that eligible providers can select to submit to CMS.

**Description:** Bedrock Physician Quality Reporting System Measure  
**Table type:** REFERENCE  
**Primary key:** `BR_PQRS_MEAS_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BR_PQRS_MEAS_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the br_pqrs_meas table. |
| 3 | `MEAS_DISPLAY` | VARCHAR(500) | NOT NULL |  | The verbiage that is displayed for the PQRS measure. |
| 4 | `MEAS_NUMBER_IDENT` | VARCHAR(50) | NOT NULL |  | Measure number (used for PQRS only). |
| 5 | `PILOT_CORE_IND` | DOUBLE | NOT NULL |  | Indicates if this is a core measure for the pilot. |
| 6 | `PILOT_ELIGIBLE_IND` | DOUBLE | NOT NULL |  | Indicates if this measure is eligible for the pilot. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_PQRS_MEAS_PROVIDER_RELTN](BR_PQRS_MEAS_PROVIDER_RELTN.md) | `BR_PQRS_MEAS_ID` |

