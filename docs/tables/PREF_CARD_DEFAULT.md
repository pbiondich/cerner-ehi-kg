# PREF_CARD_DEFAULT

> Contains attributes about a preference card default entry.

**Description:** Preference Card Default  
**Table type:** REFERENCE  
**Primary key:** `PREF_CARD_DEF_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTO_SEQ_DEF_IND` | DOUBLE |  |  | Indicates whether this default should automatically be populated in the Intraoperative Record. |
| 2 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting this row on the table |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this row was inserted on the table |
| 4 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person responsible for inserting this row on the table |
| 5 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for inserting this row on the table |
| 6 | `DEFAULT_NAME` | VARCHAR(40) |  |  | Default NameColumn |
| 7 | `ENTRY_NBR` | DOUBLE | NOT NULL |  | The entry number (sequence) for this preference card default. Only populated for repeating forms. |
| 8 | `INPUT_GROUP_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE ***Column |
| 9 | `INPUT_GROUP_SEQ` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 10 | `PREF_CARD_DEF_ID` | DOUBLE | NOT NULL | PK | The primary key, uniquely identifying a preference card default entry. |
| 11 | `PREF_CARD_SEG_ID` | DOUBLE | NOT NULL | FK→ | The documentation segment associated with this preference card default entry, i.e. Patient Positioning |
| 12 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | The input control associated with this preference card default entry. Contains a reference (foreign key) to the discrete_task_assay table. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREF_CARD_SEG_ID` | [PREF_CARD_SEGMENT](PREF_CARD_SEGMENT.md) | `PREF_CARD_SEG_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PREF_CARD_DEF_DETAIL](PREF_CARD_DEF_DETAIL.md) | `PREF_CARD_DEF_ID` |

