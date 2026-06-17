# ENCNTR_CRIMINAL_CHARGES_R

> This table will hold outstanding criminal charges for an encounter.

**Description:** ENCNTR CRIMINAL CHARGES R  
**Table type:** ACTIVITY  
**Primary key:** `OUTSTANDING_CHARGES_R_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `COURT_DT_TM` | DATETIME |  |  | The court date and time. |
| 6 | `COURT_FILE_NUM` | VARCHAR(40) |  |  | The court file number. |
| 7 | `COURT_LOCATION_CD` | DOUBLE | NOT NULL |  | The location at which the court proceedings took place. |
| 8 | `CRIMINAL_CHRG_INACTIVE_IND` | DOUBLE |  |  | Indicates whether the legal status has been inactivated by the user. |
| 9 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 10 | `OUTSTANDING_CHARGES_R_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the encntr_criminal_charges_r table. |
| 11 | `OUTSTANDING_CHARGE_CD` | DOUBLE | NOT NULL |  | Facility defined code value representing the outstanding charge for an encounter. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CRIMINAL_CHARGES_DISP_R](CRIMINAL_CHARGES_DISP_R.md) | `OUTSTANDING_CHARGES_R_ID` |

