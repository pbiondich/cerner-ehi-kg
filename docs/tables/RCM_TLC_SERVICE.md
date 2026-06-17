# RCM_TLC_SERVICE

> Contains records the facility and the service provided per encounter.

**Description:** RevWorks Care Management - Total Living Choices Service  
**Table type:** ACTIVITY  
**Primary key:** `RCM_TLC_SERVICE_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related encounter, which may be associated to many services. |
| 2 | `FINAL_TLC_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the facility that will perform the service. |
| 3 | `RCM_TLC_SERVICE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies the services provided. |
| 4 | `SERVICE_CD` | DOUBLE | NOT NULL |  | Services provided such as IV THERAPY, OXYGEN... |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `FINAL_TLC_FACILITY_ID` | [RCM_TLC_FACILITY](RCM_TLC_FACILITY.md) | `RCM_TLC_FACILITY_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RCM_TLC_SERVICE_FAC_R](RCM_TLC_SERVICE_FAC_R.md) | `RCM_TLC_SERVICE_ID` |

