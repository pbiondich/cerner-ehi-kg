# RCM_TLC_FAC_TYPE_FAC_R

> Relates Total Living Choice Facilities and the type of facility.

**Description:** RevWorks Care Management - Total Living Choices Facility & Facility Type Related  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `RCM_TLC_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related TLC facility |
| 2 | `RCM_TLC_FACILITY_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related TLC facility type. |
| 3 | `RCM_TLC_FAC_TYPE_FAC_R_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the relationship between a facility and a facility type. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RCM_TLC_FACILITY_ID` | [RCM_TLC_FACILITY](RCM_TLC_FACILITY.md) | `RCM_TLC_FACILITY_ID` |
| `RCM_TLC_FACILITY_TYPE_ID` | [RCM_TLC_FACILITY_TYPE](RCM_TLC_FACILITY_TYPE.md) | `RCM_TLC_FACILITY_TYPE_ID` |

