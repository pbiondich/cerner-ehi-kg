# CDI_WORK_ITEM_VIEW

> Stores views that can be applied to work queues. A view is a filter. When applied on a work queue, it filters items shown in a work queue based on the attributes selected to be viewable. (These attributes are saved in CDI_RULE and CDI_RULE_CRITERIA tables). Views show different users different work Items in a queue based upon the view they have selected or that is tied to their position.

**Description:** CDI Work Item View  
**Table type:** REFERENCE  
**Primary key:** `CDI_WORK_ITEM_VIEW_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_VIEW_NAME` | VARCHAR(100) | NOT NULL |  | The name of the view. |
| 2 | `CDI_VIEW_NAME_KEY` | VARCHAR(100) | NOT NULL |  | Stores corresponding string values from column CDI_VIEW_NAME for searching in UPPER case, less SPACES or special characters.. |
| 3 | `CDI_VIEW_NAME_KEY_A_NLS` | VARCHAR(400) | NOT NULL |  | Stores the corresponding non-English ACCENTED character set values for column CDI_VIEW_NAME_KEY. |
| 4 | `CDI_WORK_ITEM_VIEW_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the CDI_WORK_ITEM_VIEW table. |
| 5 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the PRSNL table. "Views" are basically filters. We have two flavors of them - user created views for their own personal use and views created by an administrator. For the personal views, the PRSNL_ID will be the user who created it and it will only be available to that user. For the views created by an administrator, the PRSNL_ID will be zero and access is based on the CDI_WORK_ITEM_POS_R table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CDI_WORK_ITEM_VIEW_POS_R](CDI_WORK_ITEM_VIEW_POS_R.md) | `CDI_WORK_ITEM_VIEW_ID` |

