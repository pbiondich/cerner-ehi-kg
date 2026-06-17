# MIC_ORGANISM_ID

> This table contains information regarding organism identifications performed on an instrument and transmitted to the Cerner system.

**Description:** Microbiology Organism Identification  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BIO_TYPE_NUMBER` | VARCHAR(100) |  |  | This field identifies the organism bio-type code sent from the susceptibility instrument interface. |
| 2 | `ID_ORGANISM_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the organism associated with the organism id task. This is the organism code that was sent to the Cerner system from the susceptibility instrument interface. The organism code received from the instrument is translated from the mic_instr_trans table and the corresponding code value is placed in this field. Organisms are defined on code set 1021. |
| 3 | `ID_SEQ` | DOUBLE | NOT NULL |  | This field contains a unique value that uniquely identifies more than one organism identification for the same task_log_id. Some instruments can send multiple identifications from which the user will make a selection as to the actual identification of the organism. |
| 4 | `ID_THRESHOLD` | DOUBLE |  |  | This field identifies the probability percentage for the organism identification. The probability is the instrument's confidence percentage on which identification is the most likely based on its biochemical reactions. This information is sent to the Cerner system from some of the susceptibility instrument interfaces. |
| 5 | `TASK_LOG_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the unique value assigned to the organism id task from the mic_task_log table thus associating the organism information with the organism id task. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ID_ORGANISM_CD` | [MIC_ORGANISM_DATA](MIC_ORGANISM_DATA.md) | `ORGANISM_ID` |
| `TASK_LOG_ID` | [MIC_TASK_LOG](MIC_TASK_LOG.md) | `TASK_LOG_ID` |

