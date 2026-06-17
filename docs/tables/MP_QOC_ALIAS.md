# MP_QOC_ALIAS

> Reference data used to alias or abreviate existing PowerOrder items used in the Quick Orders and Charges Mpage

**Description:** MPages Quick Orders and Charges Alias  
**Table type:** REFERENCE  
**Primary key:** `MP_QOC_ALIAS_ID`  
**Columns:** 15  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALIAS_DISP_NAME` | VARCHAR(255) |  |  | Shortened display for a given entity. |
| 3 | `ALIAS_THEME_COLOR_CD` | DOUBLE | NOT NULL |  | The color display theme associated to the alias. |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `FUNC_GROUPER_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | %mechinisi |
| 7 | `MP_QOC_ALIAS_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the MP_QOC_ALIAS table. |
| 8 | `ORIG_MP_QOC_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | This field is used to track versions of the aliases. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 9 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique primary identifier of the parent table. |
| 10 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The name of the parent table. Possible values: ORDER_CATALOG_SYNONYM, ORDER_SENTENCE, PATHWAY_CATALOG,PW_CAT_SYNONYM. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FUNC_GROUPER_ALIAS_ID` | [MP_QOC_ALIAS](MP_QOC_ALIAS.md) | `MP_QOC_ALIAS_ID` |
| `ORIG_MP_QOC_ALIAS_ID` | [MP_QOC_ALIAS](MP_QOC_ALIAS.md) | `MP_QOC_ALIAS_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MP_QOC_ALIAS](MP_QOC_ALIAS.md) | `FUNC_GROUPER_ALIAS_ID` |
| [MP_QOC_ALIAS](MP_QOC_ALIAS.md) | `ORIG_MP_QOC_ALIAS_ID` |

