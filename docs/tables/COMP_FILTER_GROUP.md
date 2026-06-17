# COMP_FILTER_GROUP

> Contains top level info for a set of filter parameters for a front end component.

**Description:** Component Filter Group  
**Table type:** REFERENCE  
**Primary key:** `COMP_FILTER_GROUP_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPONENT_CD` | DOUBLE | NOT NULL |  | Code value of the front end component that the filter is applicable to |
| 2 | `COMP_FILTER_GROUP_ID` | DOUBLE | NOT NULL | PK | Unique row ID |
| 3 | `FILTER_NAME` | VARCHAR(100) | NOT NULL |  | Display name of the filter group |
| 4 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | ID of the user who created the filter group. this is a PRSNL value. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [COMP_FILTER_GROUP_ITEM](COMP_FILTER_GROUP_ITEM.md) | `COMP_FILTER_GROUP_ID` |

