# ORDERS

> The table storing all orders within HNA

**Description:** ORDERS  
**Table type:** ACTIVITY  
**Primary key:** `ORDER_ID`  
**Columns:** 117  
**Referenced by:** 210 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | A grouping mechanism within catalog type code |
| 6 | `AD_HOC_ORDER_FLAG` | DOUBLE | NOT NULL |  | Flag to indicate an order is ad hoc in nature. 0 - the order is not ad hoc, 1 - the order is ad hoc via Bridge Interface, 2 - Ad hoc Order with completed order and task via Cerner Solutions, 3 - Ad hoc Order with pending task and order in ordered status via UBC (Unit-Based Cabinet). |
| 7 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The coded value for the order catalog for this order. |
| 8 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | A grouping mechanism to bring order catalogs together. |
| 9 | `CKI` | VARCHAR(255) |  |  | This field is based on the order_catalog table and is used for meds processing. The field is truncated and will contain a maximum of 254 characters. |
| 10 | `CLINICAL_DISPLAY_LINE` | VARCHAR(255) |  |  | A formatted display line of user selected order details. The field is truncated and will contain a maximum of 254 characters. When the field is truncated, it will be terminated with ellipsis. |
| 11 | `CLIN_RELEVANT_UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time when a change that is relavant to care providers was made to the order. For example, during a modify action, if the frequency is changed, then this field will get updated with the date and time when the modify was performed. |
| 12 | `CLIN_RELEVANT_UPDT_TZ` | DOUBLE | NOT NULL |  | The time zone associated with the clin_relavant_upt_dt_tm column. This is a patient centric time zone. |
| 13 | `COMMENT_TYPE_MASK` | DOUBLE |  |  | This is a mask of comment types so that we can tell what kind of comments are being used per order. |
| 14 | `CONSTANT_IND` | DOUBLE |  |  | If this indicator is set, the order is applied constantly for a period of time. Ex IV, heating pad. |
| 15 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 16 | `CS_FLAG` | DOUBLE |  |  | Bit mask on whether this order is a parent or member of a Care Set. |
| 17 | `CS_ORDER_ID` | DOUBLE | NOT NULL |  | The order of the parent of this Care Set. |
| 18 | `CURRENT_START_DT_TM` | DATETIME |  |  | The start date/time of this order. |
| 19 | `CURRENT_START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 20 | `DAY_OF_TREATMENT_SEQUENCE` | DOUBLE |  |  | The sequence of a day of treatment order. This field will be valued when the order relates to a protocol (protocol_order_id). This field will be unique across all day of treatment orders for a given protocol order ID. There is no standard pattern of sequence (i.e. increment by one) across day of treatments. |
| 21 | `DCP_CLIN_CAT_CD` | DOUBLE | NOT NULL |  | The clinical category the order is part of. |
| 22 | `DEPT_MISC_LINE` | VARCHAR(1000) |  |  | Text filled in by the department. The field is truncated and will contain a maximum of 254 characters. Ellipses are not appended if the field is truncated. |
| 23 | `DEPT_STATUS_CD` | DOUBLE | NOT NULL |  | The departmental status of the order. |
| 24 | `DISCONTINUE_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time the discontinue action should become effective. |
| 25 | `DISCONTINUE_EFFECTIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 26 | `DISCONTINUE_IND` | DOUBLE |  |  | Indicator on whether this order has been discontinued. |
| 27 | `DISCONTINUE_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates by what method the order was discontinued. |
| 28 | `DOSING_METHOD_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of dosing that is applied to the order. Values: 0 - no special dosing applies to this order, 1 - variable dosing exists for the ingredients of this order (which is only applicable for medication orders). |
| 29 | `ENCNTR_FINANCIAL_ID` | DOUBLE | NOT NULL | FK→ | The financial id for the encounter id. |
| 30 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encounter which the order is associated with. |
| 31 | `ESO_NEW_ORDER_IND` | DOUBLE |  |  | This tells the ESO server whether they have sent it outbound before or not. |
| 32 | `FORMULARY_STATUS_CD` | DOUBLE |  |  | The latest formulary status for the order's ingredients. Formulary status denotes whether an ingredient is recommended in a specific facility due to cost/availability. Formulary status will only be populated for pharmacy orders. For all non-pharmacy orders or orders for which formulary status cannot be determined, a value of 0 will be populated. All orders that exist before the concept of formulary status was introduced will have a NULL formulary status. |
| 33 | `FREQUENCY_ID` | DOUBLE | NOT NULL | FK→ | Frequency from the frequency_schedule table associated with this order. This id is used to calculate the schedule for the order. |
| 34 | `FREQ_TYPE_FLAG` | DOUBLE |  |  | Type of frequency associated with the order. |
| 35 | `FUTURE_LOCATION_FACILITY_CD` | DOUBLE | NOT NULL |  | The future facility location that is proposed to be used for this order. The facility can change while the order is in a Future status; however, once the order is activated on an encounter, this field will retain its value and will not be altered. |
| 36 | `FUTURE_LOCATION_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The future nurse unit location that is proposed to be used for this order. The nurse unit can change while the order is in a Future status; however, once the order is activated on an encounter, this field will retain its value and will not be altered. |
| 37 | `GROUP_ORDER_FLAG` | DOUBLE |  |  | A flag to note whether this order is part of a larger group. |
| 38 | `GROUP_ORDER_ID` | DOUBLE | NOT NULL |  | The order id for the parent of the group of orders. |
| 39 | `HIDE_FLAG` | DOUBLE |  |  | The order is cancelled because its parent is modified. Don't show it to the user if it's 1. |
| 40 | `HNA_ORDER_MNEMONIC` | VARCHAR(1000) |  |  | The primary mnemonic of the orderable item from which the order is created. This is the common name recognized by all clinicians who provide services to patients. For Pharmacy orders, this is the legal generic name. It normally is carried forward from primary_mnemonic field in order_catalog table. The field is truncated and will contain a maximum of 99 characters. Ellipses are not appended if the field is truncated. |
| 41 | `INCOMPLETE_ORDER_IND` | DOUBLE |  |  | When an order is in an incomplete status or would be if it weren't in an on-hold status. |
| 42 | `INGREDIENT_IND` | DOUBLE |  |  | An indicator on whether this order has multiple ingredients. |
| 43 | `INTEREST_DT_TM` | DATETIME |  |  | Currently not being used. If populated, contains the date/time for which this order should no longer appear on various reports. |
| 44 | `INTERVAL_IND` | DOUBLE |  |  | Indicates if the order is part of interval test or not. |
| 45 | `IV_IND` | DOUBLE |  |  | An indicator on whether this order is an IV. |
| 46 | `IV_SET_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The ID that uniquely identifies the IV set used to place the order. This field is only valued for IV orders that start with an IV set, and cannot be altered during subsequent order actions. |
| 47 | `LAST_ACTION_SEQUENCE` | DOUBLE |  |  | The sequence number of the last action. |
| 48 | `LAST_CORE_ACTION_SEQUENCE` | DOUBLE |  |  | Shows the last action that changed details. |
| 49 | `LAST_INGRED_ACTION_SEQUENCE` | DOUBLE |  |  | Last action sequence that contained an ingredient. |
| 50 | `LAST_UPDATE_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | The id representing the provider on the last action of the order where it was present. For example, on initial ordering if a provider id "123" is populated and then a modify action is performed on the order without populating the provider id, then this field will have a provider id of "123" which is the last valued provider id. To obtain values for each action, the provider_id from the order_action table should be read. |
| 51 | `LATEST_COMMUNICATION_TYPE_CD` | DOUBLE |  |  | CODE SET: 6006.The code value identifying the communication type of the order on the last action where it was present. For example, on initial ordering if a communication type of "FAX" is populated and then a modify action is performed on the order without populating the communication type, then this field will have a communication type of "FAX", which is the last valued communication type cd. To obtain values for each action, the communication_type_cd from the order_action should be read. |
| 52 | `LINK_NBR` | DOUBLE |  |  | Identifies a unique link and associates the orders that are members of the link. |
| 53 | `LINK_ORDER_FLAG` | DOUBLE |  |  | Flag on whether this order is linked to another. 0 - Order is not linked, 1 - Order is linked |
| 54 | `LINK_ORDER_ID` | DOUBLE | NOT NULL |  | The id of the linked order. |
| 55 | `LINK_TYPE_FLAG` | DOUBLE |  |  | Describes the kind of link the order was placed with. 0 - Not linked. 1 - AND linked. |
| 56 | `MED_ORDER_TYPE_CD` | DOUBLE | NOT NULL |  | The type of medication order. An example would be dialysis, IV, irrigation, etc. |
| 57 | `MODIFIED_START_DT_TM` | DATETIME |  |  | Date that the duration was modified. |
| 58 | `NEED_DOCTOR_COSIGN_IND` | DOUBLE |  |  | Indicator on whether a doctor needs to cosign this order. 0 - Does not need doctor cosign, 1 - Needs doctor cosign, 2 - Cosign notification is refused by doctor. |
| 59 | `NEED_NURSE_REVIEW_IND` | DOUBLE |  |  | Indicator on whether the nurse needs to cosign this order. |
| 60 | `NEED_PHYSICIAN_VALIDATE_IND` | DOUBLE |  |  | When = 0 it doesn't need a physician validation, and when = 1 needs physician validation. |
| 61 | `NEED_RX_CLIN_REVIEW_FLAG` | DOUBLE | NOT NULL |  | Indicates the clinical review status of the order. 0 - Unset, 1 - Needs Review, 2 - Review Completed, 3 - Rejected, 4 - Does Not Apply. |
| 62 | `NEED_RX_VERIFY_IND` | DOUBLE |  |  | Indicates if Pharmacy verification is needed: 0 - Does not need verification; 1 - Needs verification; 2 - Rejected or Halted. Not applicable for continuing child orders ( TEMPLATE_ORDER_FLAG of 2, 3, 4, or 6) |
| 63 | `OE_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | Id for the order entry format |
| 64 | `ORDERABLE_TYPE_FLAG` | DOUBLE |  |  | Used to store the flag that indicates what type of orderable procedure the item has been assigned. |
| 65 | `ORDERED_AS_MNEMONIC` | VARCHAR(1000) |  |  | The mnemonic used by direct care providers (physicians, nurses, etc.) when they place orders in applications such as PowerOrders. This field is important for free text orderables, since hna_order_mnemonic is a generic name and ordered_as_mnemonic carries specific information about the order. The field is truncated and will contain a maximum of 99 characters. Ellipses are not appended if the field is truncated. |
| 66 | `ORDER_COMMENT_IND` | DOUBLE |  |  | Indicator on whether this order has a comment associated with it. |
| 67 | `ORDER_DETAIL_DISPLAY_LINE` | VARCHAR(255) |  |  | The department display line for the order based on the user selected order entry fields. The field is truncated and will contain a maximum of 254 characters. Ellipses are not appended if the field is truncated. |
| 68 | `ORDER_ID` | DOUBLE | NOT NULL | PK | Order ID to which this transfer record is associated. |
| 69 | `ORDER_MNEMONIC` | VARCHAR(1000) |  |  | The mnemonic mostly used by department personnel, for example, Lab Technicians, Pharmacists. For Pharmacy orders, this field is not populated until product is assigned by Pharmacy Technician or Pharmacist. The field is truncated and will contain a maximum of 99 characters. Ellipses are not appended if the field is truncated. |
| 70 | `ORDER_REVIEW_STATUS_REASON_BIT` | DOUBLE |  |  | Indicates the reasons for the review status of the order. The first bit (2^0) indicates that the Rx verify review was removed because of the user endstate action. The second bit (2^1) indicates that the Rx verify review was removed because of the system endstate action. |
| 71 | `ORDER_SCHEDULE_PRECISION_BIT` | DOUBLE | NOT NULL |  | A bitmask which indicates the precision of the order schedule (start and stop date/times). If this mask is 0, the start and stop date/time are precise. If the mask is valued, it indicates aspects of the order schedule are estimated (not precise). The 1st bit (2^0) indicates if the start date/time is estimated. The 2nd bit (2^1) indicates if the stop date/time is estimated. |
| 72 | `ORDER_STATUS_CD` | DOUBLE | NOT NULL |  | The code for the status the order is in. |
| 73 | `ORDER_STATUS_REASON_BIT` | DOUBLE |  |  | A bitmask which indicates additional reason details about the order status. If null, there are no additional details about the status. 1-3: Incomplete to pharmacy. 4-5: Administrations. |
| 74 | `ORIGINATING_ENCNTR_ID` | DOUBLE |  | FK→ | For future orders (used for requests for consultation), Meaningful Use requires documentation of the encounter that created the future order. Since encntr_id is null for future orders (because the order will be assigned to a future encounter), a new field to track the originating encounter is needed. |
| 75 | `ORIG_ORDER_CONVS_SEQ` | DOUBLE |  |  | Stores the conversation sequence number for the new order action. This allows programs to sort by order date/time and this field to display orders to the user in the same order they were entered into the system. |
| 76 | `ORIG_ORDER_DT_TM` | DATETIME |  |  | The original order date and time for this order. |
| 77 | `ORIG_ORDER_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 78 | `ORIG_ORD_AS_FLAG` | DOUBLE |  |  | This flag shows how the order was processed by the system. This does not directly relate to the order's venue. There are cases where values of (0.0 Normal Order) and (5.0 Satellite) can be interchanged. https://wiki.cerner.com/display/public/reference/Configure+Additional+Orders+Features |
| 79 | `OVERRIDE_FLAG` | DOUBLE |  |  | Controls whether to call shareable or not. 0 - Normal process, 1 - Don't call below-the-line shareable. |
| 80 | `PATHWAY_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | Unique id from the pathway_catalog table that identifies the catalog pathway from which the order originated. |
| 81 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person whom the order is placed for. |
| 82 | `PRESCRIPTION_GROUP_VALUE` | DOUBLE |  |  | System generated ID that groups prescriptions orders belonging to the same course of treatment. |
| 83 | `PRESCRIPTION_ORDER_ID` | DOUBLE | NOT NULL | FK→ | This field applies to retail orders. It contains the order_id of the related prescription order. e.g. When a retail order is placed then the order_id of the prescription order that was used to create the retail order will be stored. |
| 84 | `PRN_IND` | DOUBLE |  |  | If this indicator is set, the order is to be be given "As needed". At the time this action occurred. |
| 85 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The product id for this order. A unique number that is system-assigned. The primary key to the product table. This column identifies the product for which the order was placed. If this column is filled out, then there is no person or encounter for this order. The product pertains to a blood product or derivative .within the PathNet Blood Bank Transfusion system. An example of an order placed. |
| 86 | `PROJECTED_STOP_DT_TM` | DATETIME |  |  | The projected stop and time for this order. |
| 87 | `PROJECTED_STOP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 88 | `PROTOCOL_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Order_id of the protocol order that generates the Day of Treatment order. 0 for protocol orders and regular (non-protocol, non-DayOfTreatment) orders. The value is decided when the order is created and cannot be changed through the life time of the order. |
| 89 | `REF_TEXT_MASK` | DOUBLE |  |  | The reference text mask showing what online reference manual components have been associated with the order. NOTE: This column does NOT support multi-facility logic. It always comes from the Order_catalog table. 1 - Policies and Procedures, 2 - Nurse Prep, 4 - Patient Education, 8 - Scheduling Info, 16 - Careplan Info, 32 - Charting Guidelines, 64 - Multum. |
| 90 | `REMAINING_DOSE_CNT` | DOUBLE |  |  | Number of doses need to be completed before the order can be completed. Currently, it is only usedwhen projected_stop_dt_tm is left empty because it can not be calculated correctly. For example, PRN orders with dose-based duration. When projected_stop_dt_tm is populated (whether in Order action,or in subsequence actions), remaining_doses is reset to 0. When remaining_doses is set to a non-zero. |
| 91 | `RESUME_EFFECTIVE_DT_TM` | DATETIME |  |  | The effective date of the resume action. |
| 92 | `RESUME_EFFECTIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 93 | `RESUME_IND` | DOUBLE |  |  | Indicator on whether this order is resumed. |
| 94 | `RX_MASK` | DOUBLE |  |  | The pharmacy mask showing how this order was placed (e.g. TPN order, Sliding Scale, Tapering Dose,etc.) 1 - Diluent (LVP), 2 - Additive (IVP), 4 - Med, 8 - TPN , 16 - Sliding Scale, 32 - Tapering Dose, 64 - PCA. |
| 95 | `SCH_STATE_CD` | DOUBLE | NOT NULL |  | Scheduling status of the order. |
| 96 | `SIMPLIFIED_DISPLAY_LINE` | VARCHAR(1000) |  |  | A simplified display line of user selected order details. The information in this field will be hard coded and only written for pharmacy orders. The field is truncated and will contain a maximum of 999 characters. When the field is truncated, it will be terminated with ellipsis. |
| 97 | `SOFT_STOP_DT_TM` | DATETIME |  |  | Filled out if an order has a stop type of hard on the order catalog. |
| 98 | `SOFT_STOP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 99 | `SOURCE_CD` | DOUBLE | NOT NULL |  | This is a codified value which identifies the source of the order. |
| 100 | `STATUS_DT_TM` | DATETIME |  |  | The date and time of the last order status change. |
| 101 | `STATUS_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel id of the person changing the status. |
| 102 | `STOP_TYPE_CD` | DOUBLE | NOT NULL |  | Codified value based on codeset 4009 indicating what type of stop is associated with this order. Ex: Physician Stop, Hard Stop, Soft Stop. |
| 103 | `SUSPEND_EFFECTIVE_DT_TM` | DATETIME |  |  | The effective suspended date time. |
| 104 | `SUSPEND_EFFECTIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 105 | `SUSPEND_IND` | DOUBLE |  |  | Indicator on whether the order is suspended. |
| 106 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | Id of the synonym for this order. |
| 107 | `TEMPLATE_CORE_ACTION_SEQUENCE` | DOUBLE |  |  | Last core action sequence of the template order. |
| 108 | `TEMPLATE_DOSE_SEQUENCE` | DOUBLE | NOT NULL |  | Relates to the template order ingredient dose from which this order was spawned. This field is only applicable for pharmacy child orders which have a variable dose (dosing_method_flag = 1). For all other orders, this field will be 0. |
| 109 | `TEMPLATE_ORDER_FLAG` | DOUBLE |  |  | Illustrates how the order relates to template orders. Valid values are: 0 - None, 1 - Template, 2 - Order Based Instance, 3 - Task Based Instance, 4 - Rx Based Instance, 5- Future Recurring Template, 6 - Future Recurring Instance, 7 - Protocol. |
| 110 | `TEMPLATE_ORDER_ID` | DOUBLE | NOT NULL |  | Order id for the template order. |
| 111 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 112 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 113 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 114 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 115 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 116 | `VALID_DOSE_DT_TM` | DATETIME |  |  | Used to capture a valid dose time of an order according its current frequency schedule. It is changed when order schedule is altered by certain actions, such as Modify and Reschedule. The field is not significant for floating schedules; however, it is populated with the time of the last action that alters the schedule. |
| 117 | `WARNING_LEVEL_BIT` | DOUBLE | NOT NULL |  | A bitmask which indicates if the order has a warning associated to it. If the bitmask is 0, no warning is associated to the order. If the mask is valued, it indicates that a warning is associated to the order. The lowest three bits indicate different level of warnings associated to the order. The 0th bit = Severe level, 1st bit = Audit level, and 2nd bit = Information level. The remaining bits will represent custom meanings (3rd bit and above). |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_FINANCIAL_ID` | [ENCNTR_FINANCIAL](ENCNTR_FINANCIAL.md) | `ENCNTR_FINANCIAL_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `FREQUENCY_ID` | [FREQUENCY_SCHEDULE](FREQUENCY_SCHEDULE.md) | `FREQUENCY_ID` |
| `IV_SET_SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |
| `LAST_UPDATE_PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `OE_FORMAT_ID` | [ORDER_ENTRY_FORMAT_PARENT](ORDER_ENTRY_FORMAT_PARENT.md) | `OE_FORMAT_ID` |
| `ORIGINATING_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PATHWAY_CATALOG_ID` | [PATHWAY_CATALOG](PATHWAY_CATALOG.md) | `PATHWAY_CATALOG_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRESCRIPTION_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |
| `PROTOCOL_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `STATUS_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

## Referenced by (210)

| From table | Column |
|------------|--------|
| [ACCESSION_ORDER_R](ACCESSION_ORDER_R.md) | `ORDER_ID` |
| [AUTH_ITEM_ORDER_RELTN](AUTH_ITEM_ORDER_RELTN.md) | `ORDER_ID` |
| [AUTH_ITEM_ORDER_R_HIST](AUTH_ITEM_ORDER_R_HIST.md) | `ORDER_ID` |
| [AV_ORDER_HOLD](AV_ORDER_HOLD.md) | `HELD_ORDER_ID` |
| [AV_ORDER_HOLD](AV_ORDER_HOLD.md) | `TRIGGER_ORDER_ID` |
| [BB_EXCEPTION](BB_EXCEPTION.md) | `ORDER_ID` |
| [BB_INVLD_PROD_ORD_EXCEPTN](BB_INVLD_PROD_ORD_EXCEPTN.md) | `PRODUCT_ORDER_ID` |
| [BB_ORDER_CELL](BB_ORDER_CELL.md) | `ORDER_ID` |
| [BB_ORDER_PHASE](BB_ORDER_PHASE.md) | `ORDER_ID` |
| [BB_WORKLIST_DETAIL](BB_WORKLIST_DETAIL.md) | `ORDER_ID` |
| [BLOT_BATCH_RESULT](BLOT_BATCH_RESULT.md) | `ORDER_ID` |
| [CE_EVENT_ORDER_LINK](CE_EVENT_ORDER_LINK.md) | `ORDER_ID` |
| [CHARGE](CHARGE.md) | `ORDER_ID` |
| [CHART_REQUEST](CHART_REQUEST.md) | `ORDER_ID` |
| [CHART_REQUEST_ORDER](CHART_REQUEST_ORDER.md) | `ORDER_ID` |
| [CONTAINER_EVENT_DETAILS](CONTAINER_EVENT_DETAILS.md) | `ORDER_ID` |
| [CONVERT_AUDIT_SYNONYM](CONVERT_AUDIT_SYNONYM.md) | `ORDER_ID` |
| [CORRECTED_PRODUCT](CORRECTED_PRODUCT.md) | `CORR_DISP_PROD_ORDER_ID` |
| [CORRECTED_PRODUCT](CORRECTED_PRODUCT.md) | `ORIG_DISP_PROD_ORDER_ID` |
| [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `ORDER_ID` |
| [CV_ED_REVIEW](CV_ED_REVIEW.md) | `ORDER_ID` |
| [CV_FAILED_TRANSACTION](CV_FAILED_TRANSACTION.md) | `ORDER_ID` |
| [CV_MED_R](CV_MED_R.md) | `PHARM_ORDER_ID` |
| [CV_PROC](CV_PROC.md) | `ORDER_ID` |
| [CV_PROC_HX](CV_PROC_HX.md) | `ORDER_ID` |
| [DISPENSE_HX](DISPENSE_HX.md) | `ORDER_ID` |
| [ECO_TEMPLATE_TRACKING](ECO_TEMPLATE_TRACKING.md) | `ORDER_ID` |
| [EEM_ABN_LINK](EEM_ABN_LINK.md) | `ORDER_ID` |
| [EKS_ALERT_ESCALATION](EKS_ALERT_ESCALATION.md) | `ORDER_ID` |
| [EKS_ALERT_ESC_HIST](EKS_ALERT_ESC_HIST.md) | `ORDER_ID` |
| [EPRESCRIBE_AUDIT](EPRESCRIBE_AUDIT.md) | `ORDER_ID` |
| [ESI_LOG](ESI_LOG.md) | `ORDER_ID` |
| [EXAM_DATA](EXAM_DATA.md) | `ORDER_ID` |
| [EXPEDITE_MANUAL](EXPEDITE_MANUAL.md) | `ORDER_ID` |
| [FILL_PRINT_ORD_HX](FILL_PRINT_ORD_HX.md) | `ORDER_ID` |
| [FOREIGN_CONTAINER](FOREIGN_CONTAINER.md) | `ORDER_ID` |
| [FOREIGN_CONTAINER_EXCPTN](FOREIGN_CONTAINER_EXCPTN.md) | `ORDER_ID` |
| [GEL_LOADING](GEL_LOADING.md) | `ORDER_ID` |
| [GEL_LOADING_POSN](GEL_LOADING_POSN.md) | `ORDER_ID` |
| [GEL_RESULT_COMMENT](GEL_RESULT_COMMENT.md) | `ORDER_ID` |
| [GROUP_ORDER_RELTN](GROUP_ORDER_RELTN.md) | `ORDER_ID` |
| [HANDHELD_DETAIL](HANDHELD_DETAIL.md) | `ORDER_ID` |
| [HIM_UNSIGNED_ORDERS](HIM_UNSIGNED_ORDERS.md) | `ORDER_ID` |
| [HLA_AB_SCREEN_RESULT](HLA_AB_SCREEN_RESULT.md) | `ORDER_ID` |
| [HLA_AB_SCREEN_WELL_SCORE](HLA_AB_SCREEN_WELL_SCORE.md) | `ORDER_ID` |
| [HLA_SERA_QUERY_SERUM](HLA_SERA_QUERY_SERUM.md) | `ORDER_ID` |
| [HLA_TYP_RES_TRAY](HLA_TYP_RES_TRAY.md) | `ORDER_ID` |
| [HLA_XM_RES_TRAY](HLA_XM_RES_TRAY.md) | `ORDER_ID` |
| [HLA_XM_TRAY_WELL](HLA_XM_TRAY_WELL.md) | `ORDER_ID` |
| [HLA_XM_TRAY_WELL_SCORE](HLA_XM_TRAY_WELL_SCORE.md) | `ORDER_ID` |
| [HLA_X_SPECIMEN_DETAIL](HLA_X_SPECIMEN_DETAIL.md) | `ORDER_ID` |
| [IB_RX_REQ_ACTION](IB_RX_REQ_ACTION.md) | `APPROVED_ORDER_ID` |
| [INFUSION_BILLING_EVENT](INFUSION_BILLING_EVENT.md) | `ORDER_ID` |
| [INFUSION_BILL_RPT_ADMIN](INFUSION_BILL_RPT_ADMIN.md) | `ORDER_ID` |
| [IO_DEVICE_INTERRUPT](IO_DEVICE_INTERRUPT.md) | `ORDER_ID` |
| [LH_CNT_IC_MED_ADMIN_EVENT](LH_CNT_IC_MED_ADMIN_EVENT.md) | `ORDER_ID` |
| [LH_CNT_IC_MED_ADMIN_EVENT](LH_CNT_IC_MED_ADMIN_EVENT.md) | `TEMPLATE_ORDER_ID` |
| [LH_CNT_IC_PATIENT_LAB](LH_CNT_IC_PATIENT_LAB.md) | `ORDER_ID` |
| [LH_CNT_IC_PATIENT_RPT_RISK](LH_CNT_IC_PATIENT_RPT_RISK.md) | `ORDER_ID` |
| [LH_CNT_IC_PATIENT_XRAY](LH_CNT_IC_PATIENT_XRAY.md) | `ORDER_ID` |
| [LH_CNT_IC_VAE_EVENT_DTL](LH_CNT_IC_VAE_EVENT_DTL.md) | `ORDER_ID` |
| [MED_ADMIN_EVENT](MED_ADMIN_EVENT.md) | `ORDER_ID` |
| [MED_ADMIN_MED_ERROR](MED_ADMIN_MED_ERROR.md) | `ORDER_ID` |
| [MED_ADMIN_RECORD](MED_ADMIN_RECORD.md) | `ORDER_ID` |
| [MESSAGING_AUDIT](MESSAGING_AUDIT.md) | `REF_ORDER_ID` |
| [MIC_IC_ORDERS](MIC_IC_ORDERS.md) | `ORDER_ID` |
| [MIC_MEDIA_LOT_RELTN](MIC_MEDIA_LOT_RELTN.md) | `ORDER_ID` |
| [MIC_ORDER_LAB](MIC_ORDER_LAB.md) | `ORDER_ID` |
| [MIC_STAT_ARCHIVE](MIC_STAT_ARCHIVE.md) | `ORDER_ID` |
| [MIC_STAT_DUPLICATE](MIC_STAT_DUPLICATE.md) | `ORDER_ID` |
| [MIC_STAT_ORDER](MIC_STAT_ORDER.md) | `ORDER_ID` |
| [MIC_TASK_LOG](MIC_TASK_LOG.md) | `ORDER_ID` |
| [OMF_RADMGMT_ORDER_ST](OMF_RADMGMT_ORDER_ST.md) | `ORDER_ID` |
| [OMF_RADREPEAT_ORDER_ST](OMF_RADREPEAT_ORDER_ST.md) | `ORDER_ID` |
| [OMF_RADREPORT_ST](OMF_RADREPORT_ST.md) | `ORDER_ID` |
| [OMF_RADTECH_ORDER_ST](OMF_RADTECH_ORDER_ST.md) | `ORDER_ID` |
| [OMF_RAD_DOSE_REPORT_DATA](OMF_RAD_DOSE_REPORT_DATA.md) | `ORDER_ID` |
| [ONC_II_AUTO_ACTIVITY](ONC_II_AUTO_ACTIVITY.md) | `ORDER_ID` |
| [ONC_INFUSION_ACTIVITY](ONC_INFUSION_ACTIVITY.md) | `ORDER_ID` |
| [ONC_TC_CAL_ITEMS](ONC_TC_CAL_ITEMS.md) | `ORDER_ID` |
| [ORDERS](ORDERS.md) | `PRESCRIPTION_ORDER_ID` |
| [ORDERS](ORDERS.md) | `PROTOCOL_ORDER_ID` |
| [ORDER_ACTION](ORDER_ACTION.md) | `ORDER_ID` |
| [ORDER_ALIAS](ORDER_ALIAS.md) | `ORDER_ID` |
| [ORDER_ATC_CODE](ORDER_ATC_CODE.md) | `ORDER_ID` |
| [ORDER_COMMENT](ORDER_COMMENT.md) | `ORDER_ID` |
| [ORDER_CONFID_LBL](ORDER_CONFID_LBL.md) | `ORDER_ID` |
| [ORDER_DAILY_REVIEW_DEFER](ORDER_DAILY_REVIEW_DEFER.md) | `ORDER_ID` |
| [ORDER_DAILY_REVIEW_HISTORY](ORDER_DAILY_REVIEW_HISTORY.md) | `ORDER_ID` |
| [ORDER_DAILY_REVIEW_RSPNL](ORDER_DAILY_REVIEW_RSPNL.md) | `ORDER_ID` |
| [ORDER_DETAIL](ORDER_DETAIL.md) | `ORDER_ID` |
| [ORDER_DETAIL_HISTORY](ORDER_DETAIL_HISTORY.md) | `ORDER_ID` |
| [ORDER_DISPENSE](ORDER_DISPENSE.md) | `ORDER_ID` |
| [ORDER_ERX_INFO](ORDER_ERX_INFO.md) | `ORDER_ID` |
| [ORDER_ERX_STATUS](ORDER_ERX_STATUS.md) | `ORDER_ID` |
| [ORDER_ERX_STATUS](ORDER_ERX_STATUS.md) | `RELATED_ORDER_ID` |
| [ORDER_EXTERNAL_IDENTIFIER](ORDER_EXTERNAL_IDENTIFIER.md) | `ORDER_ID` |
| [ORDER_FUTURE_INFO](ORDER_FUTURE_INFO.md) | `ORDER_ID` |
| [ORDER_HEALTH_PLAN](ORDER_HEALTH_PLAN.md) | `ORDER_ID` |
| [ORDER_INGREDIENT](ORDER_INGREDIENT.md) | `ORDER_ID` |
| [ORDER_INGREDIENT_HISTORY](ORDER_INGREDIENT_HISTORY.md) | `ORDER_ID` |
| [ORDER_IV_INFO](ORDER_IV_INFO.md) | `ORDER_ID` |
| [ORDER_NOTIFICATION](ORDER_NOTIFICATION.md) | `ORDER_ID` |
| [ORDER_OPS](ORDER_OPS.md) | `ORDER_ID` |
| [ORDER_ORDER_RELTN](ORDER_ORDER_RELTN.md) | `RELATED_FROM_ORDER_ID` |
| [ORDER_ORDER_RELTN](ORDER_ORDER_RELTN.md) | `RELATED_TO_ORDER_ID` |
| [ORDER_ORDER_RELTN](ORDER_ORDER_RELTN.md) | `RELTN_GROUP_ID` |
| [ORDER_PROPOSAL](ORDER_PROPOSAL.md) | `ORDER_ID` |
| [ORDER_PROPOSAL](ORDER_PROPOSAL.md) | `RELTN_GROUP_ID` |
| [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `ORDER_ID` |
| [ORDER_REVIEW](ORDER_REVIEW.md) | `ORDER_ID` |
| [ORDER_REVIEW_DECISION](ORDER_REVIEW_DECISION.md) | `ORDER_ID` |
| [ORDER_RX_SCRATCHPAD](ORDER_RX_SCRATCHPAD.md) | `RENEWED_FROM_ORDER_ID` |
| [ORDER_RX_VERIFY_INFO](ORDER_RX_VERIFY_INFO.md) | `ORDER_ID` |
| [ORDER_SCHEDULE_EXCEPTION](ORDER_SCHEDULE_EXCEPTION.md) | `ORDER_ID` |
| [ORDER_SERV_RES_CONTAINER](ORDER_SERV_RES_CONTAINER.md) | `ORDER_ID` |
| [ORDER_STAGING](ORDER_STAGING.md) | `CHARTED_ORDER_ID` |
| [ORDER_SUPPLY_REVIEW](ORDER_SUPPLY_REVIEW.md) | `ORDER_ID` |
| [ORDER_THERAP_SBSTTN](ORDER_THERAP_SBSTTN.md) | `ORDER_ID` |
| [ORDER_THERMOCYCLER_RACK](ORDER_THERMOCYCLER_RACK.md) | `ORDER_ID` |
| [ORDER_TRACKING_HIST](ORDER_TRACKING_HIST.md) | `ORDER_ID` |
| [ORDER_TRACKING_WORKLIST](ORDER_TRACKING_WORKLIST.md) | `ORDER_ID` |
| [ORDER_WARNING](ORDER_WARNING.md) | `ORDER_ID` |
| [ORD_ENTITY_RELTN](ORD_ENTITY_RELTN.md) | `ORDER_ID` |
| [ORD_RQSTN_ORD_R](ORD_RQSTN_ORD_R.md) | `ORDER_ID` |
| [ORM_ERROR_LOG](ORM_ERROR_LOG.md) | `ORDER_ID` |
| [ORM_ERX_ACTIVITY_LOG](ORM_ERX_ACTIVITY_LOG.md) | `ORDER_ID` |
| [PCS_ORDER_GROUP_R](PCS_ORDER_GROUP_R.md) | `ORDER_ID` |
| [PCS_QUEUE_ASSIGNMENT](PCS_QUEUE_ASSIGNMENT.md) | `ORDER_ID` |
| [PCS_REVIEW_ITEM](PCS_REVIEW_ITEM.md) | `ORDER_ID` |
| [PERSON_HLA_AB_SCREEN](PERSON_HLA_AB_SCREEN.md) | `ORDER_ID` |
| [PERSON_HLA_AB_SPEC](PERSON_HLA_AB_SPEC.md) | `ORDER_ID` |
| [PERSON_HLA_TYPE](PERSON_HLA_TYPE.md) | `ORDER_ID` |
| [PERSON_HLA_XM](PERSON_HLA_XM.md) | `ORDER_ID` |
| [PHA_BATCH_REPORT_ACT_DTL](PHA_BATCH_REPORT_ACT_DTL.md) | `CHILD_ORDER_ID` |
| [PHA_BATCH_REPORT_ACT_DTL](PHA_BATCH_REPORT_ACT_DTL.md) | `ORDER_ID` |
| [PHA_DISP_OBS_ST](PHA_DISP_OBS_ST.md) | `ORDER_ID` |
| [PHA_ORD_ACT_OBS_ST](PHA_ORD_ACT_OBS_ST.md) | `ORDER_ID` |
| [PHA_PROD_DISP_OBS_ST](PHA_PROD_DISP_OBS_ST.md) | `ORDER_ID` |
| [PM_PSO_LINK](PM_PSO_LINK.md) | `ORDER_ID` |
| [POSSIBLE_ANTIBODIES](POSSIBLE_ANTIBODIES.md) | `ORDER_ID` |
| [PRECOMPONENT_ORDER_RELTN](PRECOMPONENT_ORDER_RELTN.md) | `ORDER_ID` |
| [PROCEDURE_ORDER_RELTN](PROCEDURE_ORDER_RELTN.md) | `ORDER_ID` |
| [PRODUCT_EVENT](PRODUCT_EVENT.md) | `ORDER_ID` |
| [PROP_ORDER](PROP_ORDER.md) | `CS_ORDER_ID` |
| [PROP_ORDER](PROP_ORDER.md) | `ORDER_ID` |
| [PROP_RESULT](PROP_RESULT.md) | `ORDER_ID` |
| [PROTOCOL_ORDER_STAT](PROTOCOL_ORDER_STAT.md) | `FIRST_DOT_ORDER_ID` |
| [PROTOCOL_ORDER_STAT](PROTOCOL_ORDER_STAT.md) | `LAST_DOT_ORDER_ID` |
| [PROTOCOL_ORDER_STAT](PROTOCOL_ORDER_STAT.md) | `PROTOCOL_ORDER_ID` |
| [PRSNL_RELTN_ACTIVITY](PRSNL_RELTN_ACTIVITY.md) | `ORDER_ID` |
| [RAD_OMF_MAMMO](RAD_OMF_MAMMO.md) | `ORDER_ID` |
| [RAD_PACKET_COMPONENT](RAD_PACKET_COMPONENT.md) | `ORDER_ID` |
| [RAD_TECH_CMT_DATA](RAD_TECH_CMT_DATA.md) | `ORDER_ID` |
| [RAD_TECH_CMT_DATA_HIST](RAD_TECH_CMT_DATA_HIST.md) | `ORDER_ID` |
| [RAD_VETTING_HOLD_LOCK](RAD_VETTING_HOLD_LOCK.md) | `ORDER_ID` |
| [REFERRAL](REFERRAL.md) | `ORDER_ID` |
| [REFERRAL_HIST](REFERRAL_HIST.md) | `ORDER_ID` |
| [REPRINT_HX](REPRINT_HX.md) | `ORDER_ID` |
| [RESULT](RESULT.md) | `ORDER_ID` |
| [RXA_ORD_DISP_HP_OBS_ST](RXA_ORD_DISP_HP_OBS_ST.md) | `ORDER_ID` |
| [RXA_SUSPEND_ACT_LOG](RXA_SUSPEND_ACT_LOG.md) | `ORDER_ID` |
| [RXA_WORK_LOAD_OBS_ST](RXA_WORK_LOAD_OBS_ST.md) | `ORDER_ID` |
| [RXS_LOCATION_TASK](RXS_LOCATION_TASK.md) | `ORDER_ID` |
| [RXS_LOC_ENCNTR_INVENTORY](RXS_LOC_ENCNTR_INVENTORY.md) | `ORDER_ID` |
| [RXS_MED_REQUEST](RXS_MED_REQUEST.md) | `ORDER_ID` |
| [RXS_ORDER_TASK_QUEUE](RXS_ORDER_TASK_QUEUE.md) | `ORDER_ID` |
| [RX_COA_TRANS_AUDIT](RX_COA_TRANS_AUDIT.md) | `ORDER_ID` |
| [RX_DISPENSE_ORDERS_RELTN](RX_DISPENSE_ORDERS_RELTN.md) | `ORDER_ID` |
| [RX_EXT_ORD_PRD_SYNC_AUDIT](RX_EXT_ORD_PRD_SYNC_AUDIT.md) | `ORDER_ID` |
| [RX_INPT_CLAIM_HX](RX_INPT_CLAIM_HX.md) | `CHILD_ORDER_ID` |
| [RX_INPT_CLAIM_HX](RX_INPT_CLAIM_HX.md) | `ORDER_ID` |
| [RX_MED_REQUEST](RX_MED_REQUEST.md) | `ORDER_ID` |
| [RX_ORDER_REVIEW](RX_ORDER_REVIEW.md) | `ORDER_ID` |
| [RX_PENDING_CHARGE](RX_PENDING_CHARGE.md) | `ORDER_ID` |
| [RX_PENDING_REFILL](RX_PENDING_REFILL.md) | `ORDER_ID` |
| [RX_PERSON_OWE](RX_PERSON_OWE.md) | `ORDER_ID` |
| [RX_REFILL_HX](RX_REFILL_HX.md) | `ORDER_ID` |
| [RX_REFILL_TRACK_HX](RX_REFILL_TRACK_HX.md) | `ORDER_ID` |
| [RX_SCRIPT_TRANSFER_HX](RX_SCRIPT_TRANSFER_HX.md) | `ORDER_ID` |
| [RX_SCRIPT_TRANSFER_HX](RX_SCRIPT_TRANSFER_HX.md) | `XFER_ORDER_ID` |
| [RX_WORK_ITEM_QUEUE](RX_WORK_ITEM_QUEUE.md) | `ORDER_ID` |
| [RX_WORK_ITEM_QUEUE_HX](RX_WORK_ITEM_QUEUE_HX.md) | `ORDER_ID` |
| [SA_FLUID_ADMIN](SA_FLUID_ADMIN.md) | `TEMPLATE_ORDER_ID` |
| [SA_LINKED_RESULT](SA_LINKED_RESULT.md) | `ORDER_ID` |
| [SA_MEDICATION_ADMIN](SA_MEDICATION_ADMIN.md) | `TEMPLATE_ORDER_ID` |
| [SA_TODO_MEDICATION](SA_TODO_MEDICATION.md) | `ORDER_ID` |
| [SCH_PEND_ORDER](SCH_PEND_ORDER.md) | `ORDER_ID` |
| [SI_ERX_DIGITAL_SIG_LOG](SI_ERX_DIGITAL_SIG_LOG.md) | `ORDER_ID` |
| [SI_RESULT_SET_ORDER_RELTN](SI_RESULT_SET_ORDER_RELTN.md) | `ORDER_ID` |
| [SPECIMEN_USAGE](SPECIMEN_USAGE.md) | `ORDER_ID` |
| [SURG_CASE_PROCEDURE](SURG_CASE_PROCEDURE.md) | `ORDER_ID` |
| [SURG_REQ_ORDER_R](SURG_REQ_ORDER_R.md) | `ORDER_ID` |
| [SURG_REQ_PROC](SURG_REQ_PROC.md) | `ORDER_ID` |
| [TASK_ACTIVITY](TASK_ACTIVITY.md) | `CARESET_ID` |
| [TASK_ACTIVITY](TASK_ACTIVITY.md) | `ORDER_ID` |
| [TASK_ACTIVITY_MSG_H](TASK_ACTIVITY_MSG_H.md) | `ORDER_ID` |
| [TEST_REVIEWER](TEST_REVIEWER.md) | `ORDER_ID` |
| [TRACKING_EVENT_ORD](TRACKING_EVENT_ORD.md) | `ORDER_ID` |
| [UCM_CASE](UCM_CASE.md) | `ORDER_ID` |
| [UCM_CASE](UCM_CASE.md) | `STATUS_ORDER_ID` |
| [UCM_CASE_STEP](UCM_CASE_STEP.md) | `ORDER_ID` |
| [UCM_CASE_STEP](UCM_CASE_STEP.md) | `SPECIMEN_ORDER_ID` |
| [UCM_CHARGE_ORDER_R](UCM_CHARGE_ORDER_R.md) | `ORDER_ID` |
| [UCM_DSR_PANEL_INFO](UCM_DSR_PANEL_INFO.md) | `ORDER_ID` |
| [UCM_DSR_VARIANT](UCM_DSR_VARIANT.md) | `ORDER_ID` |
| [UCM_PTL_BATCH_ITEM](UCM_PTL_BATCH_ITEM.md) | `ORDER_ID` |
| [UCM_REPORT](UCM_REPORT.md) | `ORDER_ID` |
| [UCM_REPORT_FIELD](UCM_REPORT_FIELD.md) | `OD_ORDER_ID` |
| [WORKLIST_ELEMENT](WORKLIST_ELEMENT.md) | `ORDER_ID` |

