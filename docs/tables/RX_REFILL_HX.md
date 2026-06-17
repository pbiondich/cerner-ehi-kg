# RX_REFILL_HX

> History of Pending Prescriptions from Interactive Voice Response foreign system

**Description:** Prescription Refill History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 87

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_PERSONNEL_ID` | DOUBLE | NOT NULL |  | Action Personnel Id from the Order_Action table. |
| 2 | `ACTION_PROVIDER_ID` | DOUBLE | NOT NULL |  | Order Provider from the Order_Action table. |
| 3 | `ACTION_SEQUENCE` | DOUBLE |  |  | Action Sequence that last modified the Script. From the Order_Action table. |
| 4 | `AGENT_FULL_NAME` | VARCHAR(200) |  |  | The full name of the proxy prescriber for the doctoras provided on the prescription. |
| 5 | `BATCH_REFILL_DETAIL_STATUS_CD` | DOUBLE |  |  | Identifies a more detailed status for the batch refill processing |
| 6 | `BATCH_REFILL_STATUS_CD` | DOUBLE |  |  | For a Refill Request that was requested via IVR, it indicates the Overall status of request. |
| 7 | `CALLBACK_PHONE_NBR_TXT` | VARCHAR(50) | NOT NULL |  | Displays the 10-digit phone number entered by the patient. |
| 8 | `CALL_DT_TM` | DATETIME | NOT NULL |  | The date and time the patient made the call. |
| 9 | `CHILD_ORDER_ID` | DOUBLE | NOT NULL |  | Retail order that filled the Script. From Orders table. |
| 10 | `CLAIM_PROCESS_STATUS_CD` | DOUBLE |  |  | For a Refill Request that was requested via IVR, it indicates the Status of Claims Processing |
| 11 | `CLIN_CHECK_STATUS_CD` | DOUBLE |  |  | For a Refill Request that was requested via IVR, it indicates the Status of Clinical Checking Business Rules Check. |
| 12 | `COMMUNICATION_TYPE_CD` | DOUBLE | NOT NULL |  | The communication type from the Order_Action table. |
| 13 | `COMM_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates communication status |
| 14 | `CONTROL_SUBSTANCE_FLAG` | DOUBLE |  |  | identifies the controlled substance schedule for the prescribed drug. |
| 15 | `CREDIT_CARD_TXT` | VARCHAR(50) | NOT NULL |  | Credit card number used by the patient. |
| 16 | `DATE_WRITTEN_TXT` | VARCHAR(50) |  |  | The date the electronic prescription was created |
| 17 | `DAW_TXT` | VARCHAR(100) |  |  | The dispense as written text associated to the electronic prescription |
| 18 | `DEA_TXT` | VARCHAR(200) |  |  | The drug enforcement administration text associated to the electronic prescription |
| 19 | `DISPENSE_HX_ID` | DOUBLE |  | FK→ | Dispense_hx_id of the dispense row that has gone through suspend workflow - primary key of dispense_hx table |
| 20 | `DISPENSE_QTY_TXT` | VARCHAR(50) |  |  | The dispense quantity associated to the electronic prescription |
| 21 | `DISP_PRIORITY_CD` | DOUBLE | NOT NULL |  | Dispensing Priority of Refill Event |
| 22 | `DISP_PRIORITY_DT_TM` | DATETIME | NOT NULL |  | The Dispense Priority Date/Time as determined by the Dispense Priority Date/time. |
| 23 | `DISP_PRIORITY_TZ` | DOUBLE | NOT NULL |  | The time zone used in evaluating the Dispense Priority date/time |
| 24 | `DISP_SR_CD` | DOUBLE | NOT NULL |  | Service Resource tied to the pharmacy location dispensing the prescription. |
| 25 | `DR_STATUS_CD` | DOUBLE | NOT NULL |  | The Interface status of the Physician communication of the IVR Order transaction. Status types are limited to the following:1.1.1.1 Call doctor1.1.1.2 Fax sent1.1.1.3 Fax failed1.1.1.4 Notify by Pharmacy |
| 26 | `EASY_RX_PRIORITY_NBR` | DOUBLE |  |  | A value indicating the priority of the Easy Script Order. |
| 27 | `ENCNTR_ID` | DOUBLE |  | FK→ | Refers to the encounter id of the person tied to the refill request |
| 28 | `ESI_LOG_ID` | DOUBLE | NOT NULL | FK→ | Indicates related ESI_LOG record |
| 29 | `FILL_SR_CD` | DOUBLE | NOT NULL |  | Service Resource tied to the pharmacy location filling the prescription. |
| 30 | `FORMULARY_STATUS_CD` | DOUBLE |  |  | Formulary status code |
| 31 | `INTERVENTIONS_FLAG` | DOUBLE |  |  | Whether an intervention (documentation) has been done or not on prescription orders placed via powerchart. |
| 32 | `ITEM_DESC` | VARCHAR(400) |  |  | The drug description for the electronic prescription |
| 33 | `ITEM_NAME` | VARCHAR(400) |  |  | The drug mnemonic for the electronic prescription |
| 34 | `LATEST_AUTH_STATUS_CD` | DOUBLE | NOT NULL |  | The most recent status for a refill request. |
| 35 | `LATEST_NOTIFY_DT_TM` | DATETIME | NOT NULL |  | Date and time when the doctor was last notified. |
| 36 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | Med_service_cd for the Script's Encounter. From the Encounter table. |
| 37 | `MSG_IDENT_TXT` | VARCHAR(100) |  |  | The unique identifier assigned to the message by the sender. |
| 38 | `MSG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The message received from the eRx transaction. |
| 39 | `NDC_TXT` | VARCHAR(200) |  |  | The national drug code associated to the electronic prescription |
| 40 | `NOTES_TXT` | VARCHAR(250) | NOT NULL |  | Notes related to Interface transaction |
| 41 | `NOTIFY_CNT` | DOUBLE | NOT NULL |  | The number of times the doctor was notified that a request has been made for a refill. |
| 42 | `NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | Nurse_Unit_Cd for the Script's encounter. From the Encounter table. |
| 43 | `ORDER_COMMENT_IND` | DOUBLE |  |  | Indicates the existence of Order comment. |
| 44 | `ORDER_DESC` | VARCHAR(400) |  |  | The order description for the electronic prescription |
| 45 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | A unique internal identifier for this order |
| 46 | `ORDER_PRIORITY_CD` | DOUBLE | NOT NULL |  | oe_field_value with oe_field_meaning_id = 141 from Order_Detail table. |
| 47 | `PATIENT_BIRTH_DT_TXT` | VARCHAR(50) |  |  | The birth date of the patient associated to the electronic prescription |
| 48 | `PATIENT_FIRST_NAME` | VARCHAR(100) |  |  | The first name of the patient associated to the electronic prescription |
| 49 | `PATIENT_GENDER_TXT` | VARCHAR(50) |  |  | The gender of the patient |
| 50 | `PATIENT_LAST_NAME` | VARCHAR(100) |  |  | The last name of the patient associated to the electronic prescription |
| 51 | `PAYMENT_METHOD_CD` | DOUBLE | NOT NULL |  | Method of payment rendered by the patient. |
| 52 | `PERSON_ID` | DOUBLE |  | FK→ | The person for whom this refill request pertains. |
| 53 | `PHARM_CHECK_STATUS_CD` | DOUBLE |  |  | For a Refill Request that was requested via IVR, it indicates the Status of Pharmacy Refill Business Rules Check. |
| 54 | `PHYSICIAN_FIRST_NAME` | VARCHAR(100) |  |  | The first name of the doctor associated to the electronic prescription |
| 55 | `PHYSICIAN_FULL_NAME` | VARCHAR(200) |  |  | The full name of the doctor associated to the electronic prescription |
| 56 | `PHYSICIAN_LAST_NAME` | VARCHAR(100) |  |  | The last name of the doctor associated to the electronic prescription |
| 57 | `PHYSICIAN_ROUTING_SELECTION_CD` | DOUBLE |  |  | Holds the physician's prescription order mailing preference. |
| 58 | `PROJECTED_FILL_DT_TM` | DATETIME |  |  | Projected date/time when outpatient pharmacy order will be refilled. |
| 59 | `REFILL_AUTH_COMM_TYPE_CD` | DOUBLE |  |  | Identifies how the refill authorization request was communicated |
| 60 | `REFILL_NBR_TXT` | VARCHAR(50) |  |  | The number of refills for the electronic prescription |
| 61 | `REFILL_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates refill status |
| 62 | `RENEWAL_FLAG` | DOUBLE |  |  | Identifies a renewal for a prescription. |
| 63 | `RXA_PRESCRIPTION_MSG_ID` | DOUBLE |  | FK→ | The unique identifier for the electronic prescription message associated to the external prescription |
| 64 | `RXA_SUSPEND_ACT_LOG_ID` | DOUBLE |  | FK→ | This is the primary key of rxa_suspend_act_log table. Helps in getting all the suspended activity logs tied to this suspended order. |
| 65 | `RX_ACTION_DT_TM` | DATETIME |  |  | Action Date Time of the action that generated the script. From Order_Actiont able. |
| 66 | `RX_ACTION_SEQUENCE` | DOUBLE |  |  | Action Sequence that generated the Script, from Order_Action table. |
| 67 | `RX_ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | The type of action taken by the user from work queue monitor. |
| 68 | `RX_ACTION_TZ` | DOUBLE |  |  | Action time zone of the action that generated the Script. From the Order_Action table. |
| 69 | `RX_COMMENT_IND` | DOUBLE |  |  | Indicates the existence of Order comment. |
| 70 | `RX_REFILL_HX_ID` | DOUBLE | NOT NULL |  | Unique id for Rx_refill_hx table |
| 71 | `SENDER_MSG_IDENT` | DOUBLE | NOT NULL |  | *** OBSOLETE *** Has been replaced by MSG_IDENT_TXT |
| 72 | `SHORT_SIG_TXT` | VARCHAR(400) |  |  | The short version of the patient instructions |
| 73 | `SIG_TXT` | VARCHAR(4000) |  |  | The patient instructions for the electronic prescription |
| 74 | `SKIP_LOOK_FORWARD_IND` | DOUBLE |  |  | To deliver medicines through a mailer, system should process early to qualify the orders, and package and transfer through the mailer. Also, if a patient's order got qualified and the same patient is having refill for another order within a close period, we would want to bundle the orders for delivery. SKIP_LOOK_FORWARD_IND will determine whether the qualification should consider these preferences. If SKIP_LOOK_FORWARD_IND is 1, preferences will be considered, else not considered. |
| 75 | `SOURCE_TYPE_FLAG` | DOUBLE | NOT NULL |  | A flag indicating the source of the order. |
| 76 | `SUPPLY_FLAG` | DOUBLE |  |  | Identifies whether the prescription is for a supply item. |
| 77 | `SUSPEND_ROUTING_TYPE_CD` | DOUBLE |  |  | To store the specified delivery type of the medicine to the patient on the suspended order in queue. Examples: CMOP Certified Mail, Local Regular Mail, Window (in person) |
| 78 | `SUSPEND_STAGE_CD` | DOUBLE |  |  | Stores the stage in which the suspended order is in during the suspend order workflow. System will run a qualification at regular intervals to create batch of orders to be sent to CMOP location, from where the medicines will be packaged and delivered through a mailer to patients. During this process, an order will travel through various points until it reaches the patient. These points are called stages. A stage will help in identifying where the order is currently. |
| 79 | `SUSPEND_STATUS_CD` | DOUBLE |  |  | To store the status in which each suspend stage is in during the suspend order workflow |
| 80 | `SUSPEND_STATUS_DETAIL_CD` | DOUBLE |  |  | To store the failure detail type code if suspend status is fail. |
| 81 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 82 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 83 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 84 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 85 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 86 | `XRX_PATIENT_FIRST_NAME_KEY` | VARCHAR(200) |  |  | For X-Rx orders, this is the Patient's first name with all capitals and punctuation removed. Used for indexing and searching for a Patient first name |
| 87 | `XRX_PATIENT_LAST_NAME_KEY` | VARCHAR(200) |  |  | For X-Rx orders, this is Patient's last name all capitals with punctuation removed. Used for indexing and searching for a Patient by last name |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ESI_LOG_ID` | [ESI_LOG](ESI_LOG.md) | `ESI_LOG_ID` |
| `MSG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `NURSE_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RXA_PRESCRIPTION_MSG_ID` | [RXA_PRESCRIPTION_MSG](RXA_PRESCRIPTION_MSG.md) | `RXA_PRESCRIPTION_MSG_ID` |
| `RXA_SUSPEND_ACT_LOG_ID` | [RXA_SUSPEND_ACT_LOG](RXA_SUSPEND_ACT_LOG.md) | `RXA_SUSPEND_ACT_LOG_ID` |

