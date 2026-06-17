# SI_ERX_DIGITAL_SIG_LOG

> Log of information around the digital signature of ePrescribed Controlled Substance messages

**Description:** SI ePrescribe Digital Signature Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 39

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEA_NUMBER` | VARCHAR(35) |  |  | The DEA Number of the prescriber. |
| 2 | `DIGITAL_SIGNATURE` | LONGBLOB |  |  | The digital signature in binary form. |
| 3 | `DRUG_DESCRIPTION` | VARCHAR(225) |  |  | The description of the order's drug. |
| 4 | `DRUG_DIRECTIONS` | VARCHAR(1000) |  |  | The order's SIG instructions. |
| 5 | `DRUG_EFFECTIVE_DATE_TEXT` | VARCHAR(25) |  |  | The earliest fill date of the order's drug. |
| 6 | `DRUG_QUANTITY` | VARCHAR(10) |  |  | The quantity of the order's drug. |
| 7 | `DRUG_WRITTEN_DATE_TEXT` | VARCHAR(25) |  |  | The date the prescription for the drug was written. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter ID for the prescription order. |
| 9 | `MESSAGE_IDENT` | VARCHAR(30) | NOT NULL |  | The message id for the prescription message. |
| 10 | `MESSAGE_TYPE` | VARCHAR(15) | NOT NULL |  | The message type that was digitally signed |
| 11 | `NOTE` | VARCHAR(225) |  |  | The note to/from the pharmacy pertaining to this prescription. |
| 12 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order_id for the prescription order. |
| 13 | `PAT_ADDR_CITY` | VARCHAR(100) |  |  | The text name of the city associated with the patient's address. |
| 14 | `PAT_ADDR_LINE_1` | VARCHAR(100) |  |  | The first line of the patient's address. |
| 15 | `PAT_ADDR_LINE_2` | VARCHAR(100) |  |  | The second line of the patient's address. |
| 16 | `PAT_ADDR_STATE` | VARCHAR(100) |  |  | The text name of the state associated with the patient's address. |
| 17 | `PAT_ADDR_ZIPCODE` | VARCHAR(25) |  |  | The postal code associated with the patient's address. |
| 18 | `PAT_BIRTH_DATE_TEXT` | VARCHAR(25) |  |  | The text representation of the patient's date of birth in the form - YYYY-MM-DD |
| 19 | `PAT_NAME_FIRST` | VARCHAR(200) |  |  | The first name of the patient. |
| 20 | `PAT_NAME_LAST` | VARCHAR(200) |  |  | The last name of the patient. |
| 21 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the prescribed to person. |
| 22 | `PRESC_ADDR_CITY` | VARCHAR(100) |  |  | The text name of the city associated with the prescriber's address. |
| 23 | `PRESC_ADDR_LINE_1` | VARCHAR(100) |  |  | The first line of the prescriber's address. |
| 24 | `PRESC_ADDR_LINE_2` | VARCHAR(100) |  |  | The second line of the prescriber's address |
| 25 | `PRESC_ADDR_STATE` | VARCHAR(100) |  |  | The text name of the state associated with the prescriber's address. |
| 26 | `PRESC_ADDR_ZIPCODE` | VARCHAR(25) |  |  | The postal code associated with the prescriber's address. |
| 27 | `PRESC_NAME_FIRST` | VARCHAR(200) |  |  | The first name of the prescriber. |
| 28 | `PRESC_NAME_LAST` | VARCHAR(200) |  |  | The last name of the prescriber. |
| 29 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The ID of the personnel prescribing the medication. |
| 30 | `REFILL_NBR_TXT` | VARCHAR(10) |  |  | The number of refills |
| 31 | `REFILL_QUALIFIER` | VARCHAR(5) |  |  | The qualifier associated to the refills |
| 32 | `SIGNED_FIELDS` | VARCHAR(2000) | NOT NULL |  | The concatenated string comprised of the various fields that were signed. |
| 33 | `SIGN_DT_TM` | DATETIME | NOT NULL |  | The date and time that the digital signature was produced. |
| 34 | `SI_ERX_DIGITAL_SIG_LOG_ID` | DOUBLE | NOT NULL |  | Unique generated numbekr that identifies a single row on the table |
| 35 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 36 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 37 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 38 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 39 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

