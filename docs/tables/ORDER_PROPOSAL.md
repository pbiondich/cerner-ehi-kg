# ORDER_PROPOSAL

> This table stores proposal to create new orders and proposals to change existing orders. For a proposal to create a new order, there is no corresponding row on the orders table until the proposal is accepted. For all other types of proposals, there will be a corresponding row on the orders table.

**Description:** Order Proposal  
**Table type:** ACTIVITY  
**Primary key:** `ORDER_PROPOSAL_ID`  
**Columns:** 50  
**Referenced by:** 10 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BILLING_PROVIDER_FLAG` | DOUBLE | NOT NULL |  | Flag indicates which provider was specified as the billing provider. 0 - Not specified, 1 - Order provider, 2 - Supervising provider. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The catalog code from the Order_Catalog table. For a proposal to alter an existing order, this field will be in sync with the Catalog_CD field on the Orders table. |
| 3 | `CLINICAL_DISPLAY_LINE` | VARCHAR(2000) |  |  | A formatted display line of user selected order proposal details. The field is truncated and will contain a maximum of 1999 characters. When the field is truncated, it will be terminated with ellipsis. |
| 4 | `COMMUNICATION_TYPE_CD` | DOUBLE | NOT NULL |  | Codified value that identifies the means of communication which was used to generate the order proposal (how it was communicated to the proposal creator). |
| 5 | `CREATED_DT_TM` | DATETIME | NOT NULL |  | The date and time when the proposal was entered into the system. |
| 6 | `CREATED_TZ` | DOUBLE | NOT NULL |  | Time zone associated with the created_dt_tm column. |
| 7 | `DOSING_METHOD_FLAG` | DOUBLE |  |  | Indicates the type of dosing that is applied to the order proposal. Values: 0 - No special dosing applies to this order proposal, 1 - variable dosing exists for the ingredients of this order proposal (which is only applicable for medication order proposals). |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The person's encounter id. If the proposal is not associated to an encounter, the field is set to 0. For a proposal to alter an existing order, this field will be in sync with the encntr_id field on the orders table. |
| 9 | `ENTERED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The ID of the person who created this proposal. |
| 10 | `FUTURE_LOCATION_FACILITY_CD` | DOUBLE | NOT NULL |  | The future facility location that is proposed to be used for this order. The facility can change while the order is in a Future status; however, once the order is activated on an encounter, this field will retain its value and will not be altered. |
| 11 | `FUTURE_LOCATION_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The future nurse unit location that is proposed to be used for this order. The nurse unit can change while the order is in a Future status; however, once the order is activated on an encounter, this field will retain its value and will not be altered. |
| 12 | `HNA_ORDER_MNEMONIC` | VARCHAR(1000) |  |  | The primary mnemonic of the orderable item from which the order proposal is created. This is the common name recognized by all clinicians who provide services to patients. For Pharmacy order proposals, this is the legal generic name. It normally is carried forward from primary_mnemonic field in order_catalog table. The field is truncated and will contain a maximum of 999 characters. Ellipses are not appended if the field is truncated. |
| 13 | `INCOMPLETE_PROPOSAL_BIT` | DOUBLE | NOT NULL |  | A bitmask which indicates if an order proposal is incomplete in its composition. If the mask is 0, the order proposal is complete in its initial state to represent a proposed action of an order. If the mask is valued, it indicates aspects of the order proposal are incomplete and requires additional information at the time of accepting to complete its composition. Each bitmask indicates a different aspect of the proposal is incomplete (meaning, multiple aspects could be incomplete). |
| 14 | `IV_SET_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The ID that uniquely identifies the IV set used to place the proposed order action. This field may only be valued for a proposal to create a new order with an IV set or an existing order with an IV set already established. |
| 15 | `MED_ORDER_TYPE_CD` | DOUBLE | NOT NULL |  | Codified value that categorizes a medication order. For example, IV, Intermittent. For a proposal to alter an existing order, this field will be in synch with the med_order_type_cd field on the Orders table (except for Sliding Scale orders, which is identified by the rx_mask field). |
| 16 | `OE_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | The ID of the order entry format that is associated to this proposal. For a proposal to alter an existing order, this field will be in sync with the OE_Format_ID field on the Orders table. |
| 17 | `ORDERED_AS_MNEMONIC` | VARCHAR(1000) |  |  | The mnemonic used by direct care providers (physicians, nurses, etc.) when they place orders in applications such as PowerOrders. This field is important for free text orderables, since hna_order_mnemonic is a generic name and ordered_as_mnemonic carries specific information about the order. The field is truncated and will contain a maximum of 999 characters. Ellipses are not appended if the field is truncated. |
| 18 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The ID of the order associated with this proposal. If the proposal is to create a new order, the field will initially be 0 as the order does not yet exist. If the proposal is accepted, this field will be updated to the ID of the newly created order. A proposal to alter an existing order will always have a valued order id. |
| 19 | `ORDER_MNEMONIC` | VARCHAR(1000) |  |  | The mnemonic mostly used by department personnel, for example, Lab Technicians, Pharmacists. For Pharmacy orders, this field is not populated until product is assigned by Pharmacy Technician or Pharmacist. The field is truncated and will contain a maximum of 999 characters. Ellipses are not appended if the field is truncated. |
| 20 | `ORDER_PROPOSAL_ID` | DOUBLE | NOT NULL | PK | The primary key of this table. |
| 21 | `ORDER_PROPOSAL_STATUS_RSN_BIT` | DOUBLE |  |  | Bitset describing why the proposal is in a given status: Bit 0 - Invalidated due to expiration agent processing. |
| 22 | `ORDER_SCHEDULE_PRECISION_BIT` | DOUBLE | NOT NULL |  | A bitmask which indicates the precision of the order schedule (start and stop date/times). If this mask is 0, the start and stop date/time are precise. If the mask is valued, it indicates aspects of the order schedule are estimated (not precise). The 1st bit (2^0) indicates if the start date/time is estimated. The 2nd bit (2^1) indicates if the stop date/time is estimated. |
| 23 | `ORDER_STATUS_REASON_BIT` | DOUBLE |  |  | A bitmask which indicates additional reason details about the status of the proposed order. If this mask value is null, there are no additional details about the status. Bits are reserved for usage with various workflows or functionality defined below. The first bit (2^0) indicates if incomplete status has been resolved. The 2nd bit (2^1) indicates if incomplete status is due to no matching synonym. The 3rd bit (2^2) indicates if incomplete status is due to missing required details. |
| 24 | `ORIGINATING_ENCNTR_ID` | DOUBLE |  | FK→ | For future orders (used for requests for consultation), Meaningful Use requires documentation of the encounter that created the future order. Since encntr_id is null for future orders (because the order will be assigned to a future encounter), a new field to track the originating encounter is needed. |
| 25 | `ORIG_ORD_AS_FLAG` | DOUBLE | NOT NULL |  | This flag indicates how this order proposal was originally placed. For a proposal to alter an existing order, this field will be in synch with the orig_ord_as_flag on the orders table. 0 - Normal order, 1 - Prescription/Discharge order, 2 - Recorded/Home meds, 3 - Patient owns meds (this value is deprecated and will be removed in the future), 4 - Pharmacy charge only, 5 - Satellite (Super Bil) meds |
| 26 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The ID of the person for whom this proposal was made. For a proposal to alter an existing order, this field will be in sync with the person_id on the orders table. |
| 27 | `PROJECTED_CS_ORDER_ID` | DOUBLE | NOT NULL |  | The projected ID of the parent Care Set order (valued if the proposed order is a Care Set child). The ID is considered to be projected since the Care Set parent order does not have to exist in the system. |
| 28 | `PROJECTED_ORDER_ID` | DOUBLE | NOT NULL |  | This field is populated only for proposals to create new orders. If the proposal is accepted, the value from this field will become the order_id of the newly created order. |
| 29 | `PROPOSAL_FROM_ACTION_SEQ` | DOUBLE | NOT NULL |  | If the proposal is to create a new order this field will be 0. For proposals to alter an existing order, this field is the order action sequence on which this proposal is based. This is the action from which this proposal is branching. |
| 30 | `PROPOSAL_GROUP_ID` | DOUBLE | NOT NULL |  | This field is a group ID assigned if two or more proposals were processed as a group. Obsolete column |
| 31 | `PROPOSAL_SOURCE_TYPE_CD` | DOUBLE | NOT NULL |  | Codified value that indicates by what work flow the proposal was created. For example, "PHONE MESSAGE". |
| 32 | `PROPOSAL_STATUS_CD` | DOUBLE | NOT NULL |  | Codified value that indicates the status of the order proposal. |
| 33 | `PROPOSAL_TO_ACTION_SEQ` | DOUBLE | NOT NULL |  | This field will initially be set to 0. If the proposal is accepted, this field will be set to the order action sequence that is generated when the proposal is accepted. If the proposal is not accepted (rejected, withdrawn, invalidated, or never resolved) this field will remain 0. |
| 34 | `PROPOSED_ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Codified value that indicates what order action this proposal is intended to trigger. |
| 35 | `RELATED_ACTION_SEQ` | DOUBLE | NOT NULL |  | The action sequence of the existing order from which the relationship was created. Along with order_id, this field is a foreign key back to the order_action table. |
| 36 | `RELATED_ORDER_ID` | DOUBLE | NOT NULL |  | The order_id of the existing order from which the relationship was created. This field is a foreign key back to the orders table. |
| 37 | `RELATED_TYPE_CD` | DOUBLE | NOT NULL |  | Codified value that indicates the type of relationship that exists between the order and proposal. For example, Covert, etc. |
| 38 | `RELTN_GROUP_ID` | DOUBLE |  | FK→ | The relation group id for the order related to the proposal. |
| 39 | `RESOLVED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The ID of the person who resolved the proposal. |
| 40 | `RESOLVED_DT_TM` | DATETIME |  |  | The date and time when a subsequent action was taken to resolve the proposal. |
| 41 | `RESOLVED_TZ` | DOUBLE |  |  | Time zone associated with the resolved_dt_tm column. |
| 42 | `RESPONSIBLE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The ID of the person who is targeted to act on the proposal. |
| 43 | `SIMPLIFIED_DISPLAY_LINE` | VARCHAR(1000) |  |  | A simplified display line of user selected order proposal details. The information in this field will be hard coded and only written for pharmacy order proposals. The field is truncated and will contain a maximum of 999 characters. When the field is truncated, it will be terminated with ellipsis. |
| 44 | `SUPERVISING_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier represents a physician in the system who is responsible for the proposal that is placed by the mid-level provider or resident. |
| 45 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The ID that uniquely identifies the orderable associated to this proposal. For a proposal to alter an existing order, this field will be in synch with the synonym_id field on the orders table. |
| 46 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENTERED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `IV_SET_SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |
| `OE_FORMAT_ID` | [ORDER_ENTRY_FORMAT_PARENT](ORDER_ENTRY_FORMAT_PARENT.md) | `OE_FORMAT_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORIGINATING_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RELTN_GROUP_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `RESOLVED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RESPONSIBLE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SUPERVISING_PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

## Referenced by (10)

| From table | Column |
|------------|--------|
| [ORDER_PROPOSAL_ADHOC_TIME](ORDER_PROPOSAL_ADHOC_TIME.md) | `ORDER_PROPOSAL_ID` |
| [ORDER_PROPOSAL_COMMENT](ORDER_PROPOSAL_COMMENT.md) | `ORDER_PROPOSAL_ID` |
| [ORDER_PROPOSAL_CONFID_LBL](ORDER_PROPOSAL_CONFID_LBL.md) | `ORDER_PROPOSAL_ID` |
| [ORDER_PROPOSAL_DETAIL](ORDER_PROPOSAL_DETAIL.md) | `ORDER_PROPOSAL_ID` |
| [ORDER_PROPOSAL_DIAG_RELTN](ORDER_PROPOSAL_DIAG_RELTN.md) | `ORDER_PROPOSAL_ID` |
| [ORDER_PROPOSAL_INGREDIENT](ORDER_PROPOSAL_INGREDIENT.md) | `ORDER_PROPOSAL_ID` |
| [ORDER_PROPOSAL_NOTIF](ORDER_PROPOSAL_NOTIF.md) | `ORDER_PROPOSAL_ID` |
| [ORDER_PROPOSAL_THER_SBSTTN](ORDER_PROPOSAL_THER_SBSTTN.md) | `ORDER_PROPOSAL_ID` |
| [ORDER_RECON_DETAIL](ORDER_RECON_DETAIL.md) | `ORDER_PROPOSAL_ID` |
| [TASK_SUBACTIVITY](TASK_SUBACTIVITY.md) | `ORDER_PROPOSAL_ID` |

