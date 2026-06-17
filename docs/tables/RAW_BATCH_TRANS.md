# RAW_BATCH_TRANS

> Contains pre-translated x12 835 batch level data.

**Description:** Raw Batch Transactions  
**Table type:** ACTIVITY  
**Primary key:** `RAW_BATCH_TRANS_ID`  
**Columns:** 13  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_DT_TM` | DATETIME | NOT NULL |  | BPR16 - Date the originating company intends for the transaction to be settled. |
| 2 | `CONTROL_NUMBER_IDENT` | VARCHAR(30) | NOT NULL |  | Uniquely identifies the Transaction Set. Combination of ISA13, GS06, and ST02. |
| 3 | `INTERFACEID` | DOUBLE | NOT NULL |  | Used to match the INTERFACEID column on the OEN_PROCINFO table. |
| 4 | `PAYER_IDENT_CD_TXT` | VARCHAR(10) | NOT NULL |  | TRN03 - Federal tax id of the payer. |
| 5 | `PAYMENT_AMT` | DOUBLE | NOT NULL |  | BPR02 - Total Payment Amount for the Batch. |
| 6 | `PAYMENT_NUMBER_IDENT` | VARCHAR(50) | NOT NULL |  | TRN02 - Check or EFT Number. |
| 7 | `PAYMENT_TYPE_TXT` | VARCHAR(3) | NOT NULL |  | BPR04 - Type of Payment, Check or ACH. |
| 8 | `RAW_BATCH_TRANS_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a row of pre-translated X12 835 Batch Level data. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [BATCH_TRANS](BATCH_TRANS.md) | `RAW_BATCH_TRANS_ID` |
| [RAW_BATCH_TRANS_FILE](RAW_BATCH_TRANS_FILE.md) | `RAW_BATCH_TRANS_ID` |

