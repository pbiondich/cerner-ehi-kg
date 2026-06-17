# MLTM_RXB_DICTIONARY

> Multum Rx Builder Dictionary Table

**Description:** Multum Rx Builder Dictionary  
**Table type:** REFERENCE  
**Primary key:** `DICTIONARY_ID`  
**Columns:** 8  
**Referenced by:** 10 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABBREVIATION` | VARCHAR(30) |  |  | Dictionary AbbreviationColumn |
| 2 | `DESCRIPTION` | VARCHAR(255) |  |  | This field contains a textual description of each dictionary ID used in Multum's RxBuilder databases |
| 3 | `DICTIONARY_ID` | DOUBLE | NOT NULL | PK | This field contains a unique identifier for each dictionary_id used in Multum's RxBuilder tables. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (10)

| From table | Column |
|------------|--------|
| [MLTM_RXB_ORDER_DISPENSE_MAP](MLTM_RXB_ORDER_DISPENSE_MAP.md) | `DISPENSE_DICTIONARY_ID` |
| [MLTM_RXB_ORDER_DURATION_MAP](MLTM_RXB_ORDER_DURATION_MAP.md) | `DURATION_DICTIONARY_ID` |
| [MLTM_RXB_ORDER_FREQUENCY_MAP](MLTM_RXB_ORDER_FREQUENCY_MAP.md) | `FREQUENCY_DICTIONARY_ID` |
| [MLTM_RXB_ORDER_INSTRUCTION_MAP](MLTM_RXB_ORDER_INSTRUCTION_MAP.md) | `INSTRUCTION_DICTIONARY_ID` |
| [MLTM_RXB_ORDER_PRN_MAP](MLTM_RXB_ORDER_PRN_MAP.md) | `PRN_DICTIONARY_ID` |
| [MLTM_RXB_ORD_CLINICAL_RTE_MAP](MLTM_RXB_ORD_CLINICAL_RTE_MAP.md) | `CLINICAL_ROUTE_DICTIONARY_ID` |
| [MLTM_RXB_ORD_DOSE_AMOUNT](MLTM_RXB_ORD_DOSE_AMOUNT.md) | `DOSE_QTY_UNIT_DICTIONARY_ID` |
| [MLTM_RXB_ORD_DOSE_AMOUNT](MLTM_RXB_ORD_DOSE_AMOUNT.md) | `DOSE_UNIT_DICTIONARY_ID` |
| [MLTM_RXB_ORD_DOSE_RATE](MLTM_RXB_ORD_DOSE_RATE.md) | `RATE_UNIT_DICTIONARY_ID` |
| [MLTM_RXB_ORD_DOSE_RATE](MLTM_RXB_ORD_DOSE_RATE.md) | `TIME_UNIT_DICTIONARY_ID` |

