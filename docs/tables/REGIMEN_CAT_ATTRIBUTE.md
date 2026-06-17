# REGIMEN_CAT_ATTRIBUTE

> Storage for regimen attribute list. This table holds pre-defined set of attributes and display properties for those attributes.

**Description:** Regimen Catalog Attributes  
**Table type:** REFERENCE  
**Primary key:** `REGIMEN_CAT_ATTRIBUTE_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ATTRIBUTE_DISPLAY` | VARCHAR(100) | NOT NULL |  | ATTRIBUTE_DISPLAY refers to the display name for the attribute. |
| 3 | `ATTRIBUTE_MEAN` | VARCHAR(12) |  |  | ATTRIBUTE_MEAN refers to the display meaning for the attribute. RESEARCHPROT, TREATMENTINT, THERAPYLINE |
| 4 | `CODE_SET` | DOUBLE | NOT NULL | FK→ | Holds the pre defined responses for attribute. |
| 5 | `INPUT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates the input type for the attribute. 1-Yes/No 2-Codeset |
| 6 | `REGIMEN_CAT_ATTRIBUTE_ID` | DOUBLE | NOT NULL | PK | sequence name: reference_seq Unique identifier for the REGIMEN_CAT_ATTRIBUTE table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CODE_SET` | [CODE_VALUE_SET](CODE_VALUE_SET.md) | `CODE_SET` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [REGIMEN_CAT_ATTRIBUTE_R](REGIMEN_CAT_ATTRIBUTE_R.md) | `REGIMEN_CAT_ATTRIBUTE_ID` |

