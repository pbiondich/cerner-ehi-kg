# WORKLIST_REF_POS

> Stores relevant position info for laboratory worklist templates.

**Description:** Worklist Reference Position  
**Table type:** REFERENCE  
**Primary key:** `WORKLIST_REF_POS_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_ID` | DOUBLE | NOT NULL | FK→ | Indicates the unique QC accession in this template position. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `DILUTION_CD` | DOUBLE | NOT NULL |  | Contains the code value associated with this template position. |
| 4 | `NUMERIC_POSITION_TXT` | VARCHAR(10) | NOT NULL |  | The column row display for the template position, always in numeric format regardless of whether the column or row headers are defined as alpha. (i.e. 1 6, 12 5, etc.) |
| 5 | `POSITION_DISPLAY_TXT` | VARCHAR(10) | NOT NULL |  | The column row display for the template position taking into account alpha or numeric headers for the row and column. (i.e. a 6, 1 6, 1 F, etc.) |
| 6 | `POSITION_NBR` | DOUBLE | NOT NULL |  | The sequential numerical position as defined by the calling application for this template position. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `WORKLIST_REF_ID` | DOUBLE | NOT NULL | FK→ | Indicates the worklist that to which this template position belongs. |
| 13 | `WORKLIST_REF_POS_ID` | DOUBLE | NOT NULL | PK | Stores unique relevant position information for laboratory worklist templates. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCESSION_ID` | [ACCESSION](ACCESSION.md) | `ACCESSION_ID` |
| `WORKLIST_REF_ID` | [WORKLIST_REF](WORKLIST_REF.md) | `WORKLIST_REF_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [WORKLIST_POS_ORDER_R](WORKLIST_POS_ORDER_R.md) | `WORKLIST_REF_POS_ID` |

