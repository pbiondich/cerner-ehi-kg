# PRODUCT_EVENT

> Contains a row for every event that ever happened to product over its entire history, e.g., crossmatched, assigned, etc.

**Description:** Product Event  
**Table type:** ACTIVITY  
**Primary key:** `PRODUCT_EVENT_ID`  
**Columns:** 26  
**Referenced by:** 23 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BB_RESULT_ID` | DOUBLE | NOT NULL |  | An internal system-assigned number (but not a primary key to any table). Since multiple instances of a procedure can be resulted on the same patient, same accession, and same product, the BB_RESULT_ID is used to make these instances unique. |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 7 | `EVENT_DT_TM` | DATETIME |  |  | The date and time when this event occurred. |
| 8 | `EVENT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This column represents the person_id of the person from the personnel table (prsnl) who recorded this event for this product. |
| 9 | `EVENT_STATUS_FLAG` | DOUBLE |  |  | Applies only to the disposed event. The status of the disposed event, whether it has been destroyed yet or not. |
| 10 | `EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of event that occurred with the product. Pre-defined values by Cerner. Examples are: crossmatched, assigned, dispensed, etc. |
| 11 | `EVENT_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 12 | `INVENTORY_AREA_CD` | DOUBLE | NOT NULL |  | Contains the inventory area associated with product event. |
| 13 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This column represents the order_id of the order from the order table (ORDERS), if there is one associated with this event. Only certain events such as crossmatches will involve an order. |
| 14 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Contains the identifier of the organization associated with the product event. |
| 15 | `OVERRIDE_IND` | DOUBLE |  |  | Indicates whether or not an exception was overridden by the user in order to cause this event to happen with the product. Exceptions occur in the Resut Entry and Dispense applications. |
| 16 | `OVERRIDE_REASON_CD` | DOUBLE | NOT NULL |  | If an exception occurred with this event (as indicated by the OVERRIDE_IND column), this column records the reason it was overridden by the user. |
| 17 | `OWNER_AREA_CD` | DOUBLE | NOT NULL |  | Contains the owner area associated with the product event. |
| 18 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 19 | `PRODUCT_EVENT_ID` | DOUBLE | NOT NULL | PK | The primary key of this table. An internal system-assigned number that makes each row unique. |
| 20 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The primary key to the PRODUCT table. An internal system-assigned number. On this table, it identifies the product involved in the event. |
| 21 | `RELATED_PRODUCT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | This column represents the PRODUCT_EVENT_ID, which is the primary key to the PRODUCT_EVENT table. This column is used when it is necessary to associate different events with each other. One example is associating the crossmatch event with the dispense event for that patient, in which case the related product event ID on the dispense event is updated with the product_event_id from the crossmatch event. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `EVENT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |
| `RELATED_PRODUCT_EVENT_ID` | [PRODUCT_EVENT](PRODUCT_EVENT.md) | `PRODUCT_EVENT_ID` |

## Referenced by (23)

| From table | Column |
|------------|--------|
| [ABO_TESTING](ABO_TESTING.md) | `PRODUCT_EVENT_ID` |
| [ASSIGN](ASSIGN.md) | `PRODUCT_EVENT_ID` |
| [ASSIGN_RELEASE](ASSIGN_RELEASE.md) | `PRODUCT_EVENT_ID` |
| [AUTO_DIRECTED](AUTO_DIRECTED.md) | `PRODUCT_EVENT_ID` |
| [BB_DEVICE_TRANSFER](BB_DEVICE_TRANSFER.md) | `PRODUCT_EVENT_ID` |
| [BB_EXCEPTION](BB_EXCEPTION.md) | `PRODUCT_EVENT_ID` |
| [BB_EXC_CXM_PRODUCT](BB_EXC_CXM_PRODUCT.md) | `PRODUCT_EVENT_ID` |
| [BB_INVENTORY_TRANSFER](BB_INVENTORY_TRANSFER.md) | `PRODUCT_EVENT_ID` |
| [BB_INVENTORY_TRANSFER](BB_INVENTORY_TRANSFER.md) | `TO_PRODUCT_EVENT_ID` |
| [BB_SHIP_EVENT](BB_SHIP_EVENT.md) | `PRODUCT_EVENT_ID` |
| [BB_SPEC_EXP_OVRD_PROD](BB_SPEC_EXP_OVRD_PROD.md) | `PRODUCT_EVENT_ID` |
| [CORRECTED_PRODUCT](CORRECTED_PRODUCT.md) | `PRODUCT_EVENT_ID` |
| [CROSSMATCH](CROSSMATCH.md) | `PRODUCT_EVENT_ID` |
| [DESTRUCTION](DESTRUCTION.md) | `PRODUCT_EVENT_ID` |
| [DISPENSE_RETURN](DISPENSE_RETURN.md) | `PRODUCT_EVENT_ID` |
| [DISPOSITION](DISPOSITION.md) | `PRODUCT_EVENT_ID` |
| [MODIFICATION](MODIFICATION.md) | `PRODUCT_EVENT_ID` |
| [PATIENT_DISPENSE](PATIENT_DISPENSE.md) | `PRODUCT_EVENT_ID` |
| [PRODUCT_EVENT](PRODUCT_EVENT.md) | `RELATED_PRODUCT_EVENT_ID` |
| [QUARANTINE](QUARANTINE.md) | `PRODUCT_EVENT_ID` |
| [RECEIPT](RECEIPT.md) | `PRODUCT_EVENT_ID` |
| [TRANSFER](TRANSFER.md) | `PRODUCT_EVENT_ID` |
| [TRANSFUSION](TRANSFUSION.md) | `PRODUCT_EVENT_ID` |

