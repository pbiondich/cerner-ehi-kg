# SA_REF_CAT_ACTION

> Table to relate a action to the category that it falls into. Size - Based on the no. of actions they have defined. Estimate 1:1 with SA_REF_ACTION.

**Description:** SA Reference Category Action  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `SA_REF_ACTION_ID` | DOUBLE | NOT NULL | FK→ | Id of the SA action that falls under the category defined by sa_re_category_id |
| 6 | `SA_REF_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | Id of the SA category that the action belongs to |
| 7 | `SA_REF_CAT_ACTION_ID` | DOUBLE | NOT NULL |  | Unique value for the Category-Action relationship |
| 8 | `SEQUENCE` | DOUBLE |  |  | Sequence the action should be displayed in when displayed with the other actions contained within the same sa_ref_category_id |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SA_REF_ACTION_ID` | [SA_REF_ACTION](SA_REF_ACTION.md) | `SA_REF_ACTION_ID` |
| `SA_REF_CATEGORY_ID` | [SA_REF_CATEGORY](SA_REF_CATEGORY.md) | `SA_REF_CATEGORY_ID` |

