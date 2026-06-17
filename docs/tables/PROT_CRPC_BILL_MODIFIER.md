# PROT_CRPC_BILL_MODIFIER

> This table is used to store the bill modifier information for the orders that are part of a protocol

**Description:** PROTOCOL CLINICAL RESEARCH PROCESS CONTENT BILL MODIFIER  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `PROT_BILL_MODIFIER_CODE` | VARCHAR(100) |  |  | The BILL MODIFIER code for the corresponding ORDER. |
| 4 | `PROT_BILL_TO_TRIAL_CODE` | VARCHAR(100) |  |  | The BILL TO TRIAL code for the corresponding ORDER. |
| 5 | `PROT_CRPC_BILL_MODIFIER_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `PROT_MASTER_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the PROT_MASTER table. |
| 7 | `PROT_ORDER_CKI_NBR` | DOUBLE | NOT NULL |  | The unique value which helps to identify the component for an ORDER in the Power Plan XML |
| 8 | `PROT_ORDER_EXTN_TXT` | VARCHAR(140) |  |  | The unique value to identify an ORDER inside a protocol. |
| 9 | `PROT_ORDER_MNEMONIC` | VARCHAR(255) |  |  | The name of the ORDER for a protocol. A protocol can contain multiple ORDER's. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROT_MASTER_ID` | [PROT_MASTER](PROT_MASTER.md) | `PROT_MASTER_ID` |

