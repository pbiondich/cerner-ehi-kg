# SHX_CATEGORY_REF

> Each row on the table represents Social History sections.

**Description:** SHX_CATEGORY_REF  
**Table type:** REFERENCE  
**Primary key:** `SHX_CATEGORY_REF_ID`  
**Columns:** 8  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATEGORY_CD` | DOUBLE | NOT NULL | FK→ | Code set 4002165. Category code value. |
| 2 | `DESCRIPTION` | VARCHAR(100) | NOT NULL |  | Indicates description for the category |
| 3 | `SHX_CATEGORY_REF_ID` | DOUBLE | NOT NULL | PK | This is the table's primary key. The unique identifier for a Social History categories. It will be used to uniquely identify a category. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATEGORY_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SHX_ACTIVITY](SHX_ACTIVITY.md) | `SHX_CATEGORY_REF_ID` |
| [SHX_CATEGORY_DEF](SHX_CATEGORY_DEF.md) | `SHX_CATEGORY_REF_ID` |

