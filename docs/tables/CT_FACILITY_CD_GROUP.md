# CT_FACILITY_CD_GROUP

> Stores the Clinical Trials Facility Code Groupings for a CT User Preference

**Description:** CT Facility Code Groups  
**Table type:** ACTIVITY  
**Primary key:** `CT_FACILITY_CD_GROUP_ID`  
**Columns:** 8  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CT_FACILITY_CD_GROUP_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 2 | `FACILITY_CD` | DOUBLE | NOT NULL |  | Facility for this grouping |
| 3 | `FACILITY_GROUP_ID` | DOUBLE | NOT NULL | FK→ | GROUPER for set of Facilities. Value is same as PK for first facility in the group. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FACILITY_GROUP_ID` | [CT_FACILITY_CD_GROUP](CT_FACILITY_CD_GROUP.md) | `CT_FACILITY_CD_GROUP_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CT_FACILITY_CD_GROUP](CT_FACILITY_CD_GROUP.md) | `FACILITY_GROUP_ID` |
| [CT_USER_PREFERENCE](CT_USER_PREFERENCE.md) | `CT_FACILITY_CD_GROUP_ID` |

