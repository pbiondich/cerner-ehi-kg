# PRIVILEGE_DELETION

> This table is used to track deletion events in the privilege model.

**Description:** Privilege_Deletion  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_PRIVILEGE_DEF_ID` | DOUBLE | NOT NULL | FK→ | Activity_privilege_definition identifier associated with the privilege. |
| 2 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Location code value associated with the privilege. |
| 3 | `LOG_GROUPING_CD` | DOUBLE | NOT NULL |  | Logical_grouping identifier whose associated log_group_entry row(s) were deleted.Logical_grouping identifier whose associated log_group_entry row(s) were deleted.(LOGICAL_GROUPING.LOG_GROUPING_CD)CODE_SET = 0 |
| 4 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person id associated with the privilege. |
| 5 | `POSITION_CD` | DOUBLE | NOT NULL |  | Position code value associated with the privilege. |
| 6 | `PPR_CD` | DOUBLE | NOT NULL |  | Person-provider relationship code value associated with the privilege. Code Set 331 or 333. |
| 7 | `PRIVILEGE_CD` | DOUBLE | NOT NULL |  | Privilege code value associated with the privilege. |
| 8 | `PRIVILEGE_DELETION_ID` | DOUBLE | NOT NULL |  | The unique identifier of a row on this table. |
| 9 | `PRIVILEGE_ID` | DOUBLE | NOT NULL | FK→ | Identifier of the privilege that was deleted or whose exception(s) were deleted. Based on which privilege component was actually deleted, this id may or may not still exist in the privilege table |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_PRIVILEGE_DEF_ID` | [ACTIVITY_PRIVILEGE_DEFINITION](ACTIVITY_PRIVILEGE_DEFINITION.md) | `ACTIVITY_PRIVILEGE_DEF_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRIVILEGE_ID` | [PRIVILEGE](PRIVILEGE.md) | `PRIVILEGE_ID` |

