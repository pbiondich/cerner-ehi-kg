# MLTM_DDI_DESCRIPTION

> This table contains the data for drug-disease interaction text blocks and severity level.

**Description:** DDI Description  
**Table type:** REFERENCE  
**Primary key:** `DDI_ID`  
**Columns:** 10  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DDI_DESCRIPTION` | VARCHAR(4000) |  |  | Description for Drug-Drug InteractionColumn |
| 2 | `DDI_ID` | DOUBLE | NOT NULL | PK | Unique Identifier for table. Externally generated ID. No Sequence required. |
| 3 | `DDI_TITLE` | VARCHAR(100) |  |  | Title for Drug-Drug InteractionColumn |
| 4 | `FUNCTION_ID` | DOUBLE | NOT NULL |  | Multum Function Type Identifier. This will be a Foreign Key from the Multum Function_Type table when it is brought into Millennium. |
| 5 | `SEVERITY_ID_FLAG` | DOUBLE | NOT NULL |  | The severity_id identifies the severity level of the interaction described in a text block (21 = minor, 22 = moderate, 23 = major). |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [MLTM_DDI_COND_CATEGORY](MLTM_DDI_COND_CATEGORY.md) | `CHILD_COND_DDI_ID` |
| [MLTM_DDI_COND_CATEGORY](MLTM_DDI_COND_CATEGORY.md) | `PARENT_COND_DDI_ID` |
| [MLTM_DDI_MAP](MLTM_DDI_MAP.md) | `DDI_ID` |

