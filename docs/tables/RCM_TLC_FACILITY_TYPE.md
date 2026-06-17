# RCM_TLC_FACILITY_TYPE

> Stores the TLC Facility Type

**Description:** RevWorks Care Management - Total Living Choices Facility Type  
**Table type:** REFERENCE  
**Primary key:** `RCM_TLC_FACILITY_TYPE_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `RCM_TLC_FACILITY_TYPE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a TLC facility type. |
| 2 | `TLC_FACILITY_TYPE_DISPLAY` | VARCHAR(100) | NOT NULL |  | Display value for the TLC facility type. |
| 3 | `TLC_FACILITY_TYPE_IDENT` | VARCHAR(100) | NOT NULL |  | Uniquely identifies a TLC Facility Type. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RCM_TLC_FAC_TYPE_FAC_R](RCM_TLC_FAC_TYPE_FAC_R.md) | `RCM_TLC_FACILITY_TYPE_ID` |

