# WORKLIST

> Uniquely identifies a worklist.

**Description:** Worklist  
**Table type:** ACTIVITY  
**Primary key:** `WORKLIST_ID`  
**Columns:** 19  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DOWNLOADED_IND` | DOUBLE |  |  | Indicates whether or not this worklist has been downloaded at least once. |
| 2 | `SEQ_IDENT_BEG_RANGE_NBR` | DOUBLE | NOT NULL |  | Indicates the beginning instrument range sequence number when sequence identifiers are used with a given worklist. |
| 3 | `SEQ_IDENT_END_RANGE_NBR` | DOUBLE | NOT NULL |  | Indicates the ending instrument range sequence number when sequence identifiers are used with a given worklist. |
| 4 | `SEQ_IDENT_IND` | DOUBLE | NOT NULL |  | Indicates whether sequence identifiers are used with a given worklist. |
| 5 | `SEQ_IDENT_START_NBR` | DOUBLE | NOT NULL |  | Indicates the starting sequence number when sequence identifiers are used with a given worklist. |
| 6 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific service resource (such as instrument, bench, or sub-section) associated with a worklist. |
| 7 | `STATUS_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the status of an automatic worklist (e.g. building, pending, etc.). |
| 8 | `TEMPLATE_IND` | DOUBLE |  |  | Indicates whether this worklist was built using the template logic or not. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `WORKLIST_ALIAS` | VARCHAR(25) |  |  | Free-text character description for the worklist. |
| 15 | `WORKLIST_DT_TM` | DATETIME |  |  | Indicates the date and time the worklist was created. |
| 16 | `WORKLIST_ID` | DOUBLE | NOT NULL | PK | A unique, internal, system-assigned number that identifies a specific worklist. |
| 17 | `WORKLIST_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies a specific person who created the worklist. Creates a relationship to the person table. |
| 18 | `WORKLIST_REF_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies the specific worklist reference template used to create the worklist. Creates a relationship to the worklist reference table. |
| 19 | `WORKLIST_TYPE_FLAG` | DOUBLE | NOT NULL |  | Defines the type of worklist. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WORKLIST_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (9)

| From table | Column |
|------------|--------|
| [HLA_XM_RES_TRAY](HLA_XM_RES_TRAY.md) | `WORKLIST_ID` |
| [PERFORM_RESULT](PERFORM_RESULT.md) | `WORKLIST_ID` |
| [QC_RESULT](QC_RESULT.md) | `COPY_FORWARD_WORKLIST_ID` |
| [QC_RESULT](QC_RESULT.md) | `WORKLIST_ID` |
| [WORKLIST_ACCESSION_R](WORKLIST_ACCESSION_R.md) | `WORKLIST_ID` |
| [WORKLIST_ELEMENT](WORKLIST_ELEMENT.md) | `WORKLIST_ID` |
| [WORKLIST_ELEMENTS](WORKLIST_ELEMENTS.md) | `WORKLIST_ID` |
| [WORKLIST_EVENT](WORKLIST_EVENT.md) | `WORKLIST_ID` |
| [WORKLIST_ORDER_R](WORKLIST_ORDER_R.md) | `WORKLIST_ID` |

