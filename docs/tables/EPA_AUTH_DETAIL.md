# EPA_AUTH_DETAIL

> Stores Electronic Prior Authorization information Details

**Description:** Electronic Prior Authorization Details  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AUTH_EFFECTIVE_DATE_TXT` | VARCHAR(255) |  |  | The start date of the Authorization Period (character format). |
| 3 | `AUTH_EXPIRATION_DATE_TXT` | VARCHAR(255) |  |  | The end date of the Authorization Period (character format) |
| 4 | `AUTH_NOTE_ID` | DOUBLE | NOT NULL |  | **OBSOLETE** use EPA_AUTH_NOTE_ID |
| 5 | `AUTH_NUMBER_TXT` | VARCHAR(255) |  |  | The payer-assigned authorization number for the PA (character format) |
| 6 | `DAYS_SUPPLY_NBR` | DOUBLE | NOT NULL |  | This indicates the approved days supply of the requested medication. |
| 7 | `EPA_AUTH_DETAIL_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 8 | `EPA_AUTH_NOTE_ID` | DOUBLE | NOT NULL | FK→ | AUTH NOTE ID - FK Value from the EPA_LONG_TEXT table |
| 9 | `EPA_RECORD_ID` | DOUBLE | NOT NULL | FK→ | This field contains the associated EPA_RECORD identifier ( Foreign Key from EPA_RECORD) |
| 10 | `NUMBER_OF_CYCLES` | DOUBLE | NOT NULL |  | This indicates the number of dispensing cycles approved. |
| 11 | `NUMBER_OF_REFILLS` | DOUBLE | NOT NULL |  | This indicates the number of approved refills. |
| 12 | `PHARMACY_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates if only certain pharmacy types are approved to dispense the medication. 1 = Ret0ail, 2 = Mail Order, 3 = Secialty, 4 = Long Term Care, 5 = Anyo |
| 13 | `QUANTITY_UNIT_CD` | DOUBLE | NOT NULL |  | The codified value of the quantity's unit of measure. |
| 14 | `QUANTITY_VALUE` | DOUBLE | NOT NULL |  | This indicates the approved quantity of the requested medication. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EPA_AUTH_NOTE_ID` | [EPA_LONG_TEXT](EPA_LONG_TEXT.md) | `EPA_LONG_TEXT_ID` |
| `EPA_RECORD_ID` | [EPA_RECORD](EPA_RECORD.md) | `EPA_RECORD_ID` |

