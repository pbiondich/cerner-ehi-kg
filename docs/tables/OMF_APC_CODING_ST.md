# OMF_APC_CODING_ST

> omf_apc_coding_st

**Description:** The activity summary table storing the ambulatory payment classification data.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 2 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | The unique identifier for the APC code |
| 3 | `OMF_APC_CODING_ST_ID` | DOUBLE | NOT NULL |  | The unique identifier for a row on the omf_apc_coding_st |
| 4 | `RELATED_IDENTIFIER_STR` | VARCHAR(255) |  |  | The concatenation of the CPT codes that make up the APC code. |
| 5 | `RELATIVE_WEIGHT` | DOUBLE |  |  | The weight assigned to an APC code. |
| 6 | `STATUS_INDICATOR` | CHAR(1) |  |  | The status indicator for the APC code. |
| 7 | `TOTAL_EST_REIMB_VALUE` | DOUBLE |  |  | The total estimated reimbursement for the APC code. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The update application |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | The update count |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The update date/time. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The update task. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

