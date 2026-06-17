# ORDER_RX_SCRATCHPAD

> Contains prescription scratchpad orders.

**Description:** Order Prescription Scratchpad  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 42

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The coded value for the order catalog for this order. |
| 3 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific long_text record . It is a foreign key reference to the primary key of the long_text table. |
| 4 | `DISPENSE_AS_WRITTEN_IND` | DOUBLE | NOT NULL |  | Indicates if the prescription scratchpad order should be dispensed as written. |
| 5 | `DISPENSE_QUANTITY` | DOUBLE | NOT NULL |  | The dispense quantity of the prescription scratchpad order. |
| 6 | `DISPENSE_QUANTITY_UNIT_CD` | DOUBLE | NOT NULL |  | The dispense quantity unit code value of the prescription scratchpad order. |
| 7 | `DOCUMENTED_IND` | DOUBLE | NOT NULL |  | Indicates if the prescription scratchpad order is documented. |
| 8 | `DOSE` | DOUBLE | NOT NULL |  | The dose of the prescription scratchpad order. |
| 9 | `DOSE_UNIT_CD` | DOUBLE | NOT NULL |  | The dose unit code value of the prescription scratchpad order. |
| 10 | `DURATION` | DOUBLE | NOT NULL |  | The duration of the prescription scratchpad order. |
| 11 | `DURATION_UNIT_CD` | DOUBLE | NOT NULL |  | The duration unit code value of the prescription scratchpad order. |
| 12 | `FREETEXT_DOSE` | VARCHAR(1024) |  |  | The free text dose of the prescription scratchpad order. |
| 13 | `FREQUENCY_CD` | DOUBLE | NOT NULL |  | The frequency code value of the prescription scratchpad order. |
| 14 | `INCLUDE_DEA_NUMBER_IND` | DOUBLE | NOT NULL |  | Indicates if the prescription scratchpad order should include the DEA number. |
| 15 | `NO_REQUIRED_DETAILS_IND` | DOUBLE | NOT NULL |  | Indicates if the prescription scratchpad order does not need required details validated. |
| 16 | `NUMBER_OF_REFILLS` | DOUBLE | NOT NULL |  | The number of refills for the prescription scratchpad order. |
| 17 | `ORDERED_AS_MNEMONIC` | VARCHAR(1024) |  |  | The mnemonic of the prescription scratchpad order. |
| 18 | `ORDER_ENTRY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The value of the unique, internally system assigned primary identifier of the prsnl table. |
| 19 | `ORDER_ID` | DOUBLE | NOT NULL |  | The value of the unique, internally system assigned primary identifier of the orders table. |
| 20 | `ORDER_RX_SCRATCHPAD_ID` | DOUBLE | NOT NULL |  | table key The value of the unique, internally system assigned primary identifier of the order_rx_scratchpad table. |
| 21 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person whom the order is placed for. |
| 22 | `PRN_IND` | DOUBLE | NOT NULL |  | Indicates if the prescription scratchpad order is PRN. |
| 23 | `PRN_INSTRUCTIONS` | VARCHAR(1024) |  |  | The PRN instructions of the prescription scratchpad order. |
| 24 | `RENEWED_FROM_ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order_id the prescription scratchpad order is being renewed from. |
| 25 | `REQUISITION_ROUTING_CD` | DOUBLE | NOT NULL |  | The requisition routing code value of the prescription scratchpad order. |
| 26 | `RESPONSIBLE_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | The value of the unique, internally system assigned primary identifier of the prsnl table. |
| 27 | `ROUTE_OF_ADMINISTRATION_CD` | DOUBLE | NOT NULL |  | The route of administration of the prescription scratchpad order. |
| 28 | `ROUTING_PHARMACY_IDENTIFIER` | VARCHAR(100) |  |  | The unique identifier supplied from other external database - pharmacy's alphanumeric NCPDP ID. |
| 29 | `ROUTING_TYPE_FLAG` | DOUBLE |  |  | Obsolete - no longer used. The routing type of the prescription scratchpad order. |
| 30 | `SAMPLE_QUANTITY` | DOUBLE | NOT NULL |  | The sample quantity of the prescription scratchpad order. |
| 31 | `SAMPLE_QUANTITY_UNIT_CD` | DOUBLE | NOT NULL |  | The sample quantity unit code value of the prescription scratchpad order. |
| 32 | `SPECIAL_INSTRUCTIONS` | VARCHAR(1024) |  |  | The special instructions of the prescription scratchpad order. |
| 33 | `START_DT_TM` | DATETIME |  |  | The start date/time of the prescription scratchpad order |
| 34 | `STOP_DT_TM` | DATETIME |  |  | The stop date/time of the prescription scratchpad order. |
| 35 | `STOP_TYPE_CD` | DOUBLE | NOT NULL |  | The stop type code value of the prescription scratchpad order. |
| 36 | `SUPERVISING_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | In addition to order entry personnel and order provider, the system could capture a supervising provider. For example, when mid level providers (nurse practitioners) place orders, they're required to enter a supervising provider. |
| 37 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The value of the unique, internally system assigned primary identifier of the order_catalog_synonym table. |
| 38 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 39 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 40 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 41 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 42 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORDER_ENTRY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RENEWED_FROM_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `RESPONSIBLE_PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SUPERVISING_PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

