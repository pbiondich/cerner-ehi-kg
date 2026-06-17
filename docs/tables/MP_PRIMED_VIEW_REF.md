# MP_PRIMED_VIEW_REF

> Used to store Reference information about views. These views will be applied to the patients in the population table and then loaded into the activity table

**Description:** Mpages Primed Views Reference  
**Table type:** REFERENCE  
**Primary key:** `MP_PRIMED_VIEW_REF_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATEGORY_CONFIG_TXT` | VARCHAR(100) | NOT NULL |  | String to identify overall view. For summary Mpages this will be the category_mean from the br_datamart_category table. |
| 2 | `COMPONENT_CONFIG_TXT` | VARCHAR(100) | NOT NULL |  | String to identify what settings are used to load data. For summary Mpages this will be the report_mean from br_datamart_report table. |
| 3 | `DATA_GROUP_NAME` | VARCHAR(100) | NOT NULL |  | Name of sequence used to identify a view with multiple different types of data loads |
| 4 | `DATA_OBJECT_NAME` | VARCHAR(100) | NOT NULL |  | Name of CCL object used to load data for this view |
| 5 | `ENABLED_IND` | DOUBLE | NOT NULL |  | Indicates if the reference view is enabled for priming. |
| 6 | `MP_PRIMED_VIEW_REF_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the MP_PRIMED_VIEW_REF table. |
| 7 | `POP_NAME` | VARCHAR(30) | NOT NULL |  | The named population. |
| 8 | `POP_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Contains ID from referenced table e.g. TRACK_GROUP_ID |
| 9 | `POP_PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Contains table name of referenced table e.g. TRACK_GROUP. This identifies for a patient what caused them to be added to population |
| 10 | `PROXY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel Id to be used as template when applying privs |
| 11 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The ID of the personnel group category related to this view. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROXY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MP_PRIMED_VIEW_ACT](MP_PRIMED_VIEW_ACT.md) | `MP_PRIMED_VIEW_REF_ID` |

