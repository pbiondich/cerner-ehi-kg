# CNT_DCP_INTERP_STATE

> CONTENT DCP INTERPRET STATES

**Description:** CNT DCP INTERP STATE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AR_UID` | VARCHAR(100) | NOT NULL |  | CNT identifier for alpha response/nomenclature |
| 2 | `CNT_ALPHA_RESPONSE_KEY_ID` | DOUBLE | NOT NULL | FK→ | FK to CNT_ALPHA_RESPONSE_KEY |
| 3 | `CNT_DCP_INTERP_ID` | DOUBLE | NOT NULL | FK→ | Sequence generated ID - FK From CNT_DCP_INTERP |
| 4 | `CNT_DCP_INTERP_STATE_ID` | DOUBLE | NOT NULL |  | Sequence generated ID - PRIMARY KEY |
| 5 | `DCP_INTERP_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Interp |
| 6 | `FLAGS` | DOUBLE | NOT NULL |  | flags which identify properties of the component 1 - numeric component |
| 7 | `INPUT_ASSAY_UID` | VARCHAR(100) | NOT NULL |  | CNT identifier for DTA |
| 8 | `INTERP_STATE` | DOUBLE | NOT NULL |  | identifier of the state |
| 9 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | nomenclature id of input corresponding to transition_assay_cd |
| 10 | `NUMERIC_HIGH` | DOUBLE | NOT NULL |  | numeric high value |
| 11 | `NUMERIC_LOW` | DOUBLE | NOT NULL |  | numeric low value |
| 12 | `RESULTING_STATE` | DOUBLE | NOT NULL |  | next state as a result of current input |
| 13 | `RESULT_AR_UID` | VARCHAR(100) | NOT NULL |  | CNT Identifier for alpha response/nomenclature |
| 14 | `RESULT_NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Nomenclature id that should be returned as result. |
| 15 | `RESULT_VALUE` | DOUBLE | NOT NULL |  | numeric value that should be returned as a result. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNT_ALPHA_RESPONSE_KEY_ID` | [CNT_ALPHA_RESPONSE_KEY](CNT_ALPHA_RESPONSE_KEY.md) | `CNT_ALPHA_RESPONSE_KEY_ID` |
| `CNT_DCP_INTERP_ID` | [CNT_DCP_INTERP2](CNT_DCP_INTERP2.md) | `CNT_DCP_INTERP2_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `RESULT_NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

