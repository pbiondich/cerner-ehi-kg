# HLA_X_SPECIMEN_ANALYSIS

> Stores information related to a saved cross specimen analysis.

**Description:** HLA Cross Specimen Analysis  
**Table type:** ACTIVITY  
**Primary key:** `CROSS_SPECIMEN_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CROSS_SPECIMEN_DESC` | VARCHAR(250) | NOT NULL |  | Entered user-text of the analysis. |
| 2 | `CROSS_SPECIMEN_DT_TM` | DATETIME | NOT NULL |  | Date and time when the analysis was saved to the database. |
| 3 | `CROSS_SPECIMEN_ID` | DOUBLE | NOT NULL | PK | Identifier of the information related to a saved cross specimen analysis. |
| 4 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The related patient of the cross specimen analysis. |
| 5 | `POSSIBLE_ABS` | VARCHAR(250) | NOT NULL |  | User-entered text during the cross specimen analysis. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [HLA_SCREEN_ANALYSIS](HLA_SCREEN_ANALYSIS.md) | `CROSS_SPECIMEN_ID` |
| [HLA_X_SPECIMEN_DETAIL](HLA_X_SPECIMEN_DETAIL.md) | `CROSS_SPECIMEN_ID` |

