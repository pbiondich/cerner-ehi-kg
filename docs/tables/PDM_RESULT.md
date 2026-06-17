# PDM_RESULT

> Table used to hold each patient data monitoring result created.

**Description:** Patient Data Monitoring Result  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PDM_DP_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies the patient data monitoring data point created for this group of results. Creates a relationship to the patient data monitoring data point table. |
| 2 | `PERFORM_DT_TM` | DATETIME | NOT NULL |  | Stores the date and time the result was performed by the instrument or manually in Accession Result Entry. |
| 3 | `PERFORM_RESULT_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies the specific result value used. Creates a relationship to the perform result table. |
| 4 | `SEQUENCE` | DOUBLE | NOT NULL |  | Defines the sequence of results within the data point. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `ZSCORE` | DOUBLE | NOT NULL |  | Defines the value that was created for the Z Score when this row was written by pfmt_gl_to_pdm. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

