# REGIMEN_CAT_ATTRIBUTE_R

> Table is used to specify which regimen-level attributes are appropriate for each specific entry in the regimen catalog.

**Description:** Regimen catalog attribute relationship  
**Table type:** REFERENCE  
**Primary key:** `REGIMEN_CAT_ATTRIBUTE_R_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DEFAULT_VALUE_ID` | DOUBLE | NOT NULL |  | Default value ID to indentify value from table identified in DEFAULT_VALUE_NAME. This is not a translatable value for RDDS purposes if the DEFAULT_VALUE_NAME field = BOOLEAN. |
| 3 | `DEFAULT_VALUE_NAME` | VARCHAR(30) |  |  | Used to indicate whether the value in DEFAULT_VALUE_ID column refers to an actual entity in the database (i.e. code value) or an application-specific value. DEFAULT_ENTITY set to BOOLEAN means that the value in DEFAULT_VALUE column is a 0/1 type Boolean. |
| 4 | `DISPLAY_FLAG` | DOUBLE | NOT NULL |  | Display mode for the attribute on the regimen 0 = Unknown 1 = Display Only 2 = Optional 3 = Required |
| 5 | `REGIMEN_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a REGIMEN_CATALOG. It will be used to uniquely identify a regimen. foreign key from REGIMEN_CATALOG |
| 6 | `REGIMEN_CAT_ATTRIBUTE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a REGIMEN_CAT_ATTRIBUTE. It will be used to uniquely identify an attribute. foreign key from REGIMEN_CAT_ATTRIBUTE |
| 7 | `REGIMEN_CAT_ATTRIBUTE_R_ID` | DOUBLE | NOT NULL | PK | sequence name: reference_seq Unique identifier for the REGIMEN_CAT_ATTRIBUTE_R table. |
| 8 | `SEQUENCE` | DOUBLE | NOT NULL |  | Sequence of Regimen Cat Attributes within Regimen Catalog |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REGIMEN_CATALOG_ID` | [REGIMEN_CATALOG](REGIMEN_CATALOG.md) | `REGIMEN_CATALOG_ID` |
| `REGIMEN_CAT_ATTRIBUTE_ID` | [REGIMEN_CAT_ATTRIBUTE](REGIMEN_CAT_ATTRIBUTE.md) | `REGIMEN_CAT_ATTRIBUTE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [REGIMEN_ATTRIBUTE](REGIMEN_ATTRIBUTE.md) | `REGIMEN_CAT_ATTRIBUTE_R_ID` |

