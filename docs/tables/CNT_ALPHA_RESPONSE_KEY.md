# CNT_ALPHA_RESPONSE_KEY

> ALPHA RESPONSE KEY

**Description:** CNT ALPHA RESPONSE KEY  
**Table type:** REFERENCE  
**Primary key:** `CNT_ALPHA_RESPONSE_KEY_ID`  
**Columns:** 14  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AR_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Alpha Response |
| 2 | `CNT_ALPHA_RESPONSE_KEY_ID` | DOUBLE | NOT NULL | PK | PRIMERY KEY |
| 3 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | NOMENCLATURE ID - VALUE FROM NOMENCLATURE |
| 4 | `PRINCIPLE_TYPE_CD` | DOUBLE | NOT NULL |  | A general category used to group strings. (for alpha responses will be ALPHA_RESPON). |
| 5 | `PRINCIPLE_TYPE_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier FK to CNT_CODE_VALUE_KEY |
| 6 | `SOURCE_IDENTIFIER` | VARCHAR(50) |  |  | The code, or key, from the source vocabulary that contributed that string to the nomenclature (e.g. ICD9). For alpha responses, this will be blank. |
| 7 | `SOURCE_STRING` | VARCHAR(255) |  |  | Variable length string that may include alphanumeric characters and punctuation. |
| 8 | `SOURCE_VOCABULARY_CD` | DOUBLE | NOT NULL |  | The source vocabulary for the entry. |
| 9 | `SOURCE_VOCABULARY_CDUID` | VARCHAR(100) | NOT NULL |  | Unique identifier FK to CNT_CODE_VALUE_KEY |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CNT_ALPHA_RESPONSE](CNT_ALPHA_RESPONSE.md) | `CNT_ALPHA_RESPONSE_KEY_ID` |
| [CNT_DCP_INTERP_STATE](CNT_DCP_INTERP_STATE.md) | `CNT_ALPHA_RESPONSE_KEY_ID` |
| [CNT_RRF_AR_R](CNT_RRF_AR_R.md) | `CNT_ALPHA_RESPONSE_KEY_ID` |

