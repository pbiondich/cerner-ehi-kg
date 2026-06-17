# SHX_CATEGORY_DEF

> Each row on the table represents Social History category level information.

**Description:** SHX_CATEGORY_DEF  
**Table type:** REFERENCE  
**Primary key:** `SHX_CATEGORY_DEF_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `COMMENT_IND` | DOUBLE | NOT NULL |  | Indicates comment on the category. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `SHX_CATEGORY_DEF_ID` | DOUBLE | NOT NULL | PK | This is the table's primary key. The unique identifier for a Social History category. It will be used to uniquely identify a category. |
| 6 | `SHX_CATEGORY_REF_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a Social History categories. It will be used to uniquely identify a category. Foreign Key from SHX_CATEGORY_REF |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SHX_CATEGORY_REF_ID` | [SHX_CATEGORY_REF](SHX_CATEGORY_REF.md) | `SHX_CATEGORY_REF_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SHX_ACTIVITY](SHX_ACTIVITY.md) | `SHX_CATEGORY_DEF_ID` |
| [SHX_ELEMENT](SHX_ELEMENT.md) | `SHX_CATEGORY_DEF_ID` |

