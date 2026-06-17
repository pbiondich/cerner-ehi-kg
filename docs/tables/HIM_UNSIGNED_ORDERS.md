# HIM_UNSIGNED_ORDERS

> Denormalization table for orders requiring co-signature by physician.

**Description:** HIM_UNSIGNED_ORDERS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 42

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_PERSONNEL_ID` | DOUBLE | NOT NULL | FK→ | The id of the personnel that generated this action. |
| 2 | `ACTION_PRSNL_NAME` | VARCHAR(100) |  |  | Full name of the Action Personnel |
| 3 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 4 | `CONTRIBUTOR_SYSTEM_DISPLAY` | VARCHAR(40) |  |  | Display value for the Contributor system, identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 5 | `DISCH_DT_TM` | DATETIME |  |  | The actual date/time that the patient was discharged from the facility. For most outpatients, this column may be null unless the user process requires capturing this data, for example, day surgery. Auto discharge will populate this column. This also may or may not be a system assigned date and time depending on the discharge process used. |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the Encntr table identifying the encounter. |
| 7 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | The encounter type code assigned to the patient for the order. |
| 8 | `ENCNTR_TYPE_DISPLAY` | VARCHAR(40) |  |  | The display value for the encounter type. |
| 9 | `FACILITY_CD` | DOUBLE | NOT NULL | FK→ | This field is the current patient location with a location type of facility. |
| 10 | `FACILITY_NAME` | VARCHAR(40) |  |  | The name of the facility. |
| 11 | `FIN_NBR_ALIAS` | VARCHAR(200) |  |  | Financial Number alias for the encounter. |
| 12 | `HIM_UNSIGNED_ORDERS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the HIM_UNSIGNED_ORDERS table. |
| 13 | `LAST_COMM_TYPE_DISPLAY` | VARCHAR(40) |  |  | The latest communication type display value. |
| 14 | `LATEST_COMMUNICATION_TYPE_CD` | DOUBLE |  |  | CODE SET: 6006.The code value identifying the communication type of the order on the last action where it was present. For example, on initial ordering if a communication type of "FAX" is populated and then a modify action is performed on the order without populating the communication type, then this field will have a communication type of "FAX", which is the last valued communication type cd. To obtain values for each action, the communication_type_cd from the order_action should be read. |
| 15 | `MRN_ALIAS` | VARCHAR(200) |  |  | Person level medical record number. |
| 16 | `NOTIFICATION_DT_TM` | DATETIME |  |  | The time that the notification is created. |
| 17 | `NOTIFICATION_TZ` | DOUBLE |  |  | Time Zone the notification date and time should be displayed in. |
| 18 | `ORDERED_AS_MNEMONIC` | VARCHAR(1000) |  |  | The mnemonic used by direct care providers (physicians, nurses, etc.) when they place orders in applications such as PowerOrders. This field is important for free text orderables, since hna_order_mnemonic is a generic name and ordered_as_mnemonic carries specific information about the order. The field is truncated and will contain a maximum of 99 characters. Ellipses are not appended if the field is truncated. |
| 19 | `ORDER_ACTION_DT_TM` | DATETIME |  |  | The Date and Time of the order action. |
| 20 | `ORDER_ACTION_SEQ` | DOUBLE | NOT NULL |  | The action sequence at the time of task for tasks with an order_id context. |
| 21 | `ORDER_ACTION_TZ` | DOUBLE |  |  | Time Zone to apply to the Order Action Date and Time. |
| 22 | `ORDER_DT_TM` | DATETIME |  |  | The original order date and time for this order. |
| 23 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The id of the order. |
| 24 | `ORDER_NOTIFICATION_ID` | DOUBLE | NOT NULL | FK→ | Unique ID for Order_Notification. |
| 25 | `ORDER_STATUS_CD` | DOUBLE | NOT NULL |  | The code for the status the order is in. |
| 26 | `ORDER_STATUS_DISPLAY` | VARCHAR(40) |  |  | The display value from the order_status _cd. |
| 27 | `ORDER_TZ` | DOUBLE |  |  | Time Zone of the user who placed the order. |
| 28 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. This column is either valued with the facility or the client organization for the encounter. |
| 29 | `ORGANIZATION_NAME` | VARCHAR(100) |  |  | The name of the organization. |
| 30 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 31 | `PERSON_NAME_FULL_FORMATTED` | VARCHAR(100) |  |  | Full name of the Person |
| 32 | `REG_DT_TM` | DATETIME |  |  | Registration date/time of encounter. |
| 33 | `TO_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The PERSON_ID of the person from the personnel table (PRSNL) to whom the notification should be sent. |
| 34 | `TO_PRSNL_NAME_FULL_FORMATTED` | VARCHAR(100) |  |  | Full name of the Personnel to sign the Order. |
| 35 | `TO_PRSNL_ROLE_CD` | DOUBLE | NOT NULL |  | Default Role of the Personnel to sign the order. |
| 36 | `TO_PRSNL_ROLE_DISPLAY` | VARCHAR(40) |  |  | Display for the default role of the personnel to sign the order. |
| 37 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PERSONNEL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORDER_NOTIFICATION_ID` | [ORDER_NOTIFICATION](ORDER_NOTIFICATION.md) | `ORDER_NOTIFICATION_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `TO_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

