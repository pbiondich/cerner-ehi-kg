# DD_SDOC_GROUPBY

> This table contains the documented GroupBy and SGroupBy elements in a structured section.

**Description:** Dynamic Documentation Structured Documentation Group By  
**Table type:** ACTIVITY  
**Primary key:** `DD_SDOC_GROUPBY_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DD_SDOC_GROUPBY_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a documented GroupBy or SGroupBy element in a structured section. |
| 2 | `DD_SDOC_SECTION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related section. |
| 3 | `GROUP_LABEL` | VARCHAR(3000) | NOT NULL |  | The label of this Group (typically displayed at the top of the Group). |
| 4 | `PARENT_DD_SDOC_GROUPBY_ID` | DOUBLE | NOT NULL | FK→ | The id of the parent Group. This will be equal to the DD_SDOC_GROUPBY_ID when this is a top-level group. For a subgroup, it will be equal to the parent group's DD_SDOC_GROUPBY_ID id. |
| 5 | `TRUTH_STATE_CD` | DOUBLE | NOT NULL |  | Truth state of this Group - options defined on codeset 15751. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DD_SDOC_SECTION_ID` | [DD_SDOC_SECTION](DD_SDOC_SECTION.md) | `DD_SDOC_SECTION_ID` |
| `PARENT_DD_SDOC_GROUPBY_ID` | [DD_SDOC_GROUPBY](DD_SDOC_GROUPBY.md) | `DD_SDOC_GROUPBY_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DD_SDOC_GROUPBY](DD_SDOC_GROUPBY.md) | `PARENT_DD_SDOC_GROUPBY_ID` |
| [DD_SDOC_ITEM](DD_SDOC_ITEM.md) | `PARENT_DD_SDOC_GROUPBY_ID` |

