# IB_RX_REQ_DIAGNOSIS

> Contains the diagnosis information for the prescription request on the inbound pharmacy request.

**Description:** Inbound RX Request Diagnosis  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DIAGNOSIS_SEQ` | DOUBLE | NOT NULL |  | Preserves the order the diagnosis list was received from the pharmacy. |
| 2 | `DIAGNOSIS_SOURCE_NAME` | VARCHAR(255) |  |  | The person or pharmacy that added the diagnosis to the request. |
| 3 | `IB_RX_REQ_DIAGNOSIS_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies an individual row on the IB_RX_REQ_DIAGNOSIS table. |
| 4 | `IB_RX_REQ_DRUG_ID` | DOUBLE | NOT NULL | FK→ | The drug for this diagnosis. |
| 5 | `IB_RX_REQ_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE **** |
| 6 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier from nomenclature table, which is used to identify the diagnosis. |
| 7 | `NOMEN_SOURCE_IDENT_VALUE` | VARCHAR(255) |  |  | The diagnosis on the incoming request. |
| 8 | `NOMEN_STRING_SOURCE_CD` | DOUBLE | NOT NULL |  | Represents the external source that owns the nomen_source_ident_value. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IB_RX_REQ_DRUG_ID` | [IB_RX_REQ_DRUG](IB_RX_REQ_DRUG.md) | `IB_RX_REQ_DRUG_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

