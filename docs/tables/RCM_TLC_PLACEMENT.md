# RCM_TLC_PLACEMENT

> Stores the facaility the patient was placed for discharge.

**Description:** RevWorks Care Management - Total Living Choices Placement  
**Table type:** ACTIVITY  
**Primary key:** `RCM_TLC_PLACEMENT_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related encounter |
| 4 | `FINAL_TLC_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the facility at which the patient will be placed. |
| 5 | `RCM_TLC_PLACEMENT_ID` | DOUBLE | NOT NULL | PK | Records and contains the facility the patient was placed at for discharge. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `FINAL_TLC_FACILITY_ID` | [RCM_TLC_FACILITY](RCM_TLC_FACILITY.md) | `RCM_TLC_FACILITY_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RCM_TLC_PLACEMENT_FAC_R](RCM_TLC_PLACEMENT_FAC_R.md) | `RCM_TLC_PLACEMENT_ID` |

