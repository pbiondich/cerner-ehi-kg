# ORDER_HEALTH_PLAN

> Claims related information for a Health Plan of a given Order action

**Description:** Order Health Plan  
**Table type:** ACTIVITY  
**Primary key:** `ACTION_SEQUENCE`, `CARD_HOLDER_IDENT`, `HEALTH_PLAN_ID`, `ORDER_ID`  
**Columns:** 66  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL | PK | A sequence number used to identify the order of the actions. |
| 2 | `ACTUAL_DAYS_SUPPLY` | DOUBLE | NOT NULL |  | Estimated number of days the prescription will last. |
| 3 | `ALTERNATE_IDENT` | VARCHAR(250) | NOT NULL |  | Person identifier to be used for controlled product reporting. Identifier may be that of the patient or the person picking up the prescription as required by the governing body sent in field 330-cw of claim segment (07) |
| 4 | `ASSOC_PRESCRIP_DT_TM` | DATETIME |  |  | Date of the Associated Prescription/ Service Reference Number.Field 457-EP on Claim Segment (07) |
| 5 | `ASSOC_PRESCRIP_NBR` | VARCHAR(200) | NOT NULL |  | Related 'Prescription/Service Reference Number' To which the service is associated. Field 456-EN on Claim Segment (07) |
| 6 | `ASSOC_PRESCRIP_TZ` | DOUBLE | NOT NULL |  | Time zone for the assoc_prescrip_dt_tm |
| 7 | `AUTH_NBR_TXT` | VARCHAR(250) | NOT NULL |  | Number assigned by the processor to identify an authorized transaction sent in field 503-f3 of prior auth segment (12) |
| 8 | `AUTH_REP_CITY` | VARCHAR(250) | NOT NULL |  | State/Province of the patient's authorized representative sent in field 498-PJ or prior auth segment (12) |
| 9 | `AUTH_REP_FIRST_NAME` | VARCHAR(250) | NOT NULL |  | First name of the patient's authorized representative sent in field 498-PE of prior auth segment (12). |
| 10 | `AUTH_REP_LAST_NAME` | VARCHAR(250) | NOT NULL |  | Last name of the patient's authorized representative sent in field 498-PE of prior auth segment (12) |
| 11 | `AUTH_REP_STATE` | VARCHAR(250) | NOT NULL |  | State/Province of the patient's authorized representative sent in field 498-PJ of prior auth segment (12) |
| 12 | `AUTH_REP_STREET` | VARCHAR(250) | NOT NULL |  | Street address of the patient's authorized representative sent in field 498-PG of prior auth segment (12) |
| 13 | `AUTH_REP_ZIP` | VARCHAR(250) | NOT NULL |  | Zip code/Postal zone of the patient's authorized representative sent in field 498-PK of prior auth segment (12) |
| 14 | `CARD_HOLDER_IDENT` | VARCHAR(100) | NOT NULL | PK | The member number of the subscriber to the health plan. |
| 15 | `COB_OTHER_PAYER_PAY_AMT` | DOUBLE | NOT NULL |  | Amount of any payment known by the pharmacy from other sources (including coupons). Sent in field 431-DV of claim segment. |
| 16 | `COB_OTHER_PAYER_PAY_TYPE_CD` | DOUBLE | NOT NULL |  | Service type of payment that the Other Payer amount was applied to. Example: Delivery, Drug Benefit. Sent in field 342-HC of claim segment. |
| 17 | `COB_PAYER_CTRL_IDENT` | VARCHAR(30) |  |  | Used to identify an adjudicated claim, when supplied, in payer-to-payer coordination of benefits only. Sent in field 993-A7 of claim segment. |
| 18 | `COMPOUND_FORM_CD` | DOUBLE | NOT NULL |  | Dosage form for the complete compound mixture as prescribed by NDCPD format. |
| 19 | `CONFLICT_CD` | DOUBLE | NOT NULL |  | DUR Conflict code |
| 20 | `COUPON_AMT` | DOUBLE | NOT NULL |  | Value of coupon sent in field 487-NE of coupon segment (09) |
| 21 | `COUPON_NBR_TXT` | VARCHAR(250) | NOT NULL |  | Unique serial number assigned to the prescription coupons sent in field 486-ME of coupon segment (09) |
| 22 | `COUPON_TYPE_CD` | DOUBLE | NOT NULL |  | Code Indicating the type of coupon being used sent in field 485-KE of coupon segment (09) |
| 23 | `DUR_AGENT_QUAL_CD` | DOUBLE | NOT NULL |  | Drug Utilization Review Co-Agent Id Qualifier for Retail Prescription Claims |
| 24 | `DUR_AGENT_QUAL_IDENT` | VARCHAR(30) | NOT NULL |  | Drug Utilization Review Co-Agent Id for Retail Prescription Claims |
| 25 | `DUR_LEVEL_OF_EFFORT_CD` | DOUBLE | NOT NULL |  | Code indicating the level of effort as determined by the complexity of decision making or resources utilized by a pharmacist to perform a professional service sent in field 474-8E of DUR/PPS segment (08). |
| 26 | `ELIGIBILITY_CD` | DOUBLE | NOT NULL |  | Eligibility Clarification Code |
| 27 | `EMPLOYER_IDENT` | VARCHAR(250) | NOT NULL |  | ID assigned to an employer sent in field 333_CZ of patient segment (01) |
| 28 | `FACILITY_IDENT` | VARCHAR(250) | NOT NULL |  | ID assigned to the patient's clinic/host party sent in field 336-8C of insurance segment (04) |
| 29 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | PK FK→ | Identifier assigned for a Health Plan |
| 30 | `HEALTH_PLAN_SEQ` | DOUBLE | NOT NULL |  | Sequence in which Health Plan is used during claim submission. |
| 31 | `HOME_PLAN_IDENT` | VARCHAR(250) | NOT NULL |  | Code identifying the Blue Cross or Blue Shield plan ID which indicates where the member's coverage has been designated. Usually where the member lives or purchased their coverage. Sent in field 314-CE of the insurance segment (04). |
| 32 | `INTERVENTION_CD` | DOUBLE | NOT NULL |  | DUR Intervention Code |
| 33 | `INTER_AUTH_IDENT` | VARCHAR(250) | NOT NULL |  | Value indicating intermediary authorization occurred sent in field 464-EX of claim segment (07) |
| 34 | `INTER_AUTH_TYPE_ID_CD` | DOUBLE | NOT NULL |  | Value indicating that authorization occurred for intermediary processing sent in field 463-EW of claim segment (07) |
| 35 | `LEVEL_OF_SERVICE_CD` | DOUBLE | NOT NULL |  | Code indicating the type of service the provider rendered sent in field 418-DI of claim segment (07) |
| 36 | `MANUAL_ADJUDICATED_IND` | DOUBLE | NOT NULL |  | Indicates whether the adjudication is manual or electronic for plans that are part of Benefits Coordination. 0 - Electronic, 1 - Manual |
| 37 | `MANUAL_COPAY_AMT` | DOUBLE | NOT NULL |  | Copay Amount for manually adjudicated plans that are part of Benefits Coordination. |
| 38 | `ORDER_ID` | DOUBLE | NOT NULL | PK FK→ | This field contains the unique value assigned to each orderable procedure associated with an order. |
| 39 | `ORIG_PRESCRIBED_QTY` | DOUBLE | NOT NULL |  | Product initially prescribed amount expressed in metric decimal units sent in field 446-EB of claim segment (07) |
| 40 | `ORIG_PRESCRIBED_SERV_QUAL_CD` | DOUBLE | NOT NULL |  | Code qualifying the value in the Originally Prescribed Product/Service Code sent . |
| 41 | `ORIG_PRESCRIBED_SERV_QUAL_TXT` | VARCHAR(250) | NOT NULL |  | Code of the initially prescribed product of service sent in field 445-EA of claim segment (07) |
| 42 | `OTHER_COVERAGE_CD` | DOUBLE | NOT NULL |  | Other coverage code accept in Order Entry |
| 43 | `OUTCOME_CD` | DOUBLE | NOT NULL |  | DUR Outcome code |
| 44 | `PARTIAL_FILL_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates if a health plan supports NCPDP 51 Partial Fill Submission Process. |
| 45 | `PATIENT_LOCATION_ID_CD` | DOUBLE | NOT NULL |  | The code identifying the location of the patient when receiving Pharmacy Services sent in field 307-C7 of patient segment (01) |
| 46 | `PATIENT_PAID_AMT` | DOUBLE | NOT NULL |  | The amount the pharmacy received from the patient for the prescription dispensed sent in field 433-DX of pricing segment (11) |
| 47 | `PA_REQ_BASIS_CD` | DOUBLE | NOT NULL |  | Prior Authorized Basis of Request for Retail Prescription Claims. |
| 48 | `PA_REQ_BEG_DT_TM` | DATETIME |  |  | Prior Authorized Request Period Begin Date and Time for Retail Prescription claims. |
| 49 | `PA_REQ_END_DT_TM` | DATETIME |  |  | Prior Authorized Request Period End Date and Time for Retail Prescription claims. |
| 50 | `PA_REQ_TYPE_CD` | DOUBLE | NOT NULL |  | Prior Authorized Request Type for Retail Prescription Claims |
| 51 | `PA_REQ_TZ` | DOUBLE | NOT NULL |  | Time zone for the pa_req_beg_dt_tm and pa_req_end_dt_tm. |
| 52 | `PRESCRIPTION_CD` | DOUBLE | NOT NULL |  | Prescription clarification code |
| 53 | `PRIOR_AUTH_BEG_EFF_DT_TM` | DATETIME |  |  | Effective Date from date of prior authorization number |
| 54 | `PRIOR_AUTH_END_EFF_DT_TM` | DATETIME |  |  | Effective To date of prior authorization number |
| 55 | `PRIOR_AUTH_NBR_ASSIGN_TXT` | VARCHAR(250) | NOT NULL |  | Unique number identifying the prior authorization assigned by the processor sent field 498-PY of prior auth segment. |
| 56 | `PRIOR_AUTH_NBR_TXT` | VARCHAR(250) | NOT NULL |  | Prior authorization number |
| 57 | `PRIOR_AUTH_SUPPORT_DOC_TXT` | VARCHAR(500) | NOT NULL |  | Free text message sent in field 498-PP of prior auth segment (12) |
| 58 | `PRIOR_AUTH_TYPE_CD` | DOUBLE | NOT NULL |  | NCPDP Prior Authorization Type Code |
| 59 | `PRIOR_AUTH_TZ` | DOUBLE | NOT NULL |  | Time zone for the prior_auth_beg_eff_dt_tm and prior_auth_end_eff_dt_tm. |
| 60 | `SCHED_PRESCRIPT_ID_NBR_TXT` | VARCHAR(250) | NOT NULL |  | The serial number of the prescription blank/form sent in field 454-EK of claim segment (07) |
| 61 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 62 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 63 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 64 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 65 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 66 | `WORKERS_COMP_FLAG` | DOUBLE | NOT NULL |  | Workers Compensation segment flag indicates whether or not the segment is required to transmit. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

## Referenced by (8)

| From table | Column |
|------------|--------|
| [ORDER_HEALTH_PLAN_DETAIL](ORDER_HEALTH_PLAN_DETAIL.md) | `ACTION_SEQ` |
| [ORDER_HEALTH_PLAN_DETAIL](ORDER_HEALTH_PLAN_DETAIL.md) | `CARD_HOLDER_IDENT` |
| [ORDER_HEALTH_PLAN_DETAIL](ORDER_HEALTH_PLAN_DETAIL.md) | `HEALTH_PLAN_ID` |
| [ORDER_HEALTH_PLAN_DETAIL](ORDER_HEALTH_PLAN_DETAIL.md) | `ORDER_ID` |
| [RX_CLAIM_PENDING](RX_CLAIM_PENDING.md) | `ACTION_SEQUENCE_NBR` |
| [RX_CLAIM_PENDING](RX_CLAIM_PENDING.md) | `CARD_HOLDER_IDENT` |
| [RX_CLAIM_PENDING](RX_CLAIM_PENDING.md) | `HEALTH_PLAN_ID` |
| [RX_CLAIM_PENDING](RX_CLAIM_PENDING.md) | `ORDER_ID` |

