# RXA_PRESCRIPTION_MSG_HX

> Stores prescription message history information

**Description:** Pharmacy Outpatient Prescription Message History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTROL_SUBSTANCE_CLASS_FLAG` | DOUBLE | NOT NULL |  | Identifies the controlled substance schedule for the prescribed drug |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date and time when the row was inserted |
| 3 | `DIGITAL_SIGNATURE_FLAG` | DOUBLE | NOT NULL |  | Identifies whether the prescription has been digitally signed |
| 4 | `DRUG_NAME` | VARCHAR(300) |  |  | Drug name contained in the message |
| 5 | `MSG_CLOB` | LONGTEXT |  |  | Prescription message text that pertains to a specific transaction type |
| 6 | `MSG_DOCTOR_SPI_TXT` | VARCHAR(50) |  |  | The doctor's Surescripts Provider Identifier contained in the message |
| 7 | `MSG_FORMAT_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the format type of the message |
| 8 | `MSG_IDENT` | VARCHAR(100) |  |  | The identifier assigned to the message by the sender which can be external or internal to our system. For externally received messages, our system will append the prescriber SPI to the end of the message identifier separated by an underscore. The orig_msg_ident column will only contain the message identifier with no value appended to it. |
| 9 | `MSG_NABP_TXT` | VARCHAR(50) |  |  | The pharmacy's NABP number contained in the message |
| 10 | `ORIG_MSG_IDENT` | VARCHAR(100) |  |  | The identifier assigned to the message by the sender which can be external or internal to our system. |
| 11 | `PATIENT_FIRST_NAME` | VARCHAR(100) |  |  | First name of the patient contained in the message |
| 12 | `PATIENT_LAST_NAME` | VARCHAR(100) |  |  | Last name of the patient contained in the message |
| 13 | `PHYSICIAN_DEA_TXT` | VARCHAR(50) |  |  | The doctor's Drug Enforcement Administration number contained in the message |
| 14 | `PHYSICIAN_FIRST_NAME` | VARCHAR(100) |  |  | First name of the doctor contained in the message |
| 15 | `PHYSICIAN_LAST_NAME` | VARCHAR(100) |  |  | Last name of the doctor contained in the message |
| 16 | `PHYSICIAN_NPI_TXT` | VARCHAR(50) |  |  | The doctor's National Provider Identifier contained in the message |
| 17 | `REF_RXA_PRESCRIPTION_MSG_ID` | DOUBLE | NOT NULL |  | Identifies the reference prescription message identifier that this row relates to |
| 18 | `RXA_PRESCRIPTION_MSG_HX_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RXA_PRESCRIPTION_MSG_HX table. |
| 19 | `RXA_PRESCRIPTION_MSG_ID` | DOUBLE | NOT NULL |  | Unique generated number that identified a single row on the rxa_prescription_msg table before moving to the history table |
| 20 | `RX_MSG_TRANS_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the transaction type of the message (ie. NEWRX, REFREQ, REFRES, ERROR, STATUS, VERIFY) |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

